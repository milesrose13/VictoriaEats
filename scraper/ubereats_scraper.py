from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from tqdm import tqdm
import requests
from datetime import date
import csv

BASE_URL = 'https://www.ubereats.com'

class MenuItems:
    def __init__(self, dish_id, name, description, price, restaurant_id):
        self.dish_id = dish_id
        self.name = name
        self.description = description
        self.price = price
        self.restaurant_id = restaurant_id
    
    def __str__(self):
        return f"Dish name: {clean_text(self.name)}\nDish price:{self.price}\nRestaurant:{self.restaurant_id}\nDescription:{clean_text(self.description)}"

class VictoriaRestaurants:
    def __init__(self, id, name, description, address, created_on, menu_page_url):
        self.id = id
        self.name = name
        self.description = description
        self.address = address
        self.city = 'Victoria'
        self.created_on = created_on
        self.menu_page_url = menu_page_url
        
    def __str__(self):
        return f"Restaurant: {clean_text(self.name)}\nDescription: {self.description}\nAddress: {self.address}\nCity: {self.city}\nURL:{clean_text(self.menu_page_url)}\n\n\n"

def write_restaurants_to_csv(restaurants, filename):
    header = ['restaurant_id', 'name', 'description', 'address', 'city', 'created_on']
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(header)
        
        # Write the restaurant data
        for restaurant in restaurants:
            writer.writerow([restaurant.id, restaurant.name, restaurant.description, restaurant.address, restaurant.city, restaurant.created_on])
            
def write_menu_items_to_csv(menu_items, filename):
    header = ['dish_id', 'name', 'description', 'price', 'restaurant_id']
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(header)
        
        # Write the menu item data
        for item in menu_items:
            writer.writerow([item.dish_id, item.name, item.description, item.price, item.restaurant_id])

def clean_text(text):
    # Replace problematic characters with a placeholder
    return text.encode('ascii', errors='ignore').decode('ascii')

def clean_menu_urls(menu_urls: list[str]) -> list[str]:
    """
    Brief: filters collected urls to only get restaurant
    menu urls. Menu urls refer to the url that take us to
    the restaurants actual UberEats page, which contains 
    all food items offered by the restaurant.
    
    Params: menu_urls (list[str]): a list of all the urls
    in the <a> tag on the webpage.
    
    Return: filtered_menu_urls (list[str]): list of all the 
    menu URLs.
    """
    filtered_menu_urls = []
    for menu_url in menu_urls:
        url = menu_url.get('href')
        if url is not None and url.startswith('/ca/store/'):
            filtered_menu_urls.append(url)
    return filtered_menu_urls

def get_restaurant_names_with_menu_urls(url: str) -> tuple[list[VictoriaRestaurants], list[MenuItems]]:
    """
    Brief: finds all the restaurants in Victoria, BC listed on 
    UberEats (with the restaurants' urls) and then stores them in a list.
    
    Params: url (str): the UberEats webpage that lists all available
    restaurants in Victoria, BC.
    
    Returns: restaurants (list[VictoriaRestaurants]): a list of the 
    found restaurants with their respective URLs. 
    """
    req = Request(url, headers = {'User-agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    
    soup = BeautifulSoup(page, 'html.parser')    
    urls = soup.findAll('a')
    menu_urls = clean_menu_urls(urls)
    
    restaurants = []
    menu_items = []
    url_index = 0
    descriptions_and_addresses = soup.findAll('span')

    descriptions_and_addresses_index = 0
    
    for i, restaurant in enumerate(tqdm(soup.findAll('h3')), 0):
        if restaurant.text.endswith('?'):
            continue
        id = i
        clean_name = clean_text(restaurant.text)
        
        # Spans contain three different types of information:
        # Category, Description, and Address
        # We only want the description and address and will skip the category
        if (descriptions_and_addresses_index + 2 < len(descriptions_and_addresses)):
            description = clean_text(descriptions_and_addresses[descriptions_and_addresses_index + 1].text)
            address = clean_text(descriptions_and_addresses[descriptions_and_addresses_index + 2].text)
            descriptions_and_addresses_index += 3
        
        date_added_to_db = date.today()
        restaurant = VictoriaRestaurants(id, clean_name, description, address, date_added_to_db, menu_urls[url_index])
        url_index += 1
        
        restaurant_menu = extract_restaurant_menu_itmes(restaurant)
        if restaurant_menu is not None:
            menu_items.extend(restaurant_menu)
            restaurants.append(restaurant)
        else:
            continue
        
    return (restaurants, menu_items)


def extract_restaurant_menu_itmes(restaurant_metadata: VictoriaRestaurants) -> list[MenuItems]:
    menu_items = []
    
    url = BASE_URL + restaurant_metadata.menu_page_url
    restaurant_id = restaurant_metadata.id
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to load page{url}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    main_div = soup.find('div', {'id': 'store-desktop-menu-nav'})
    
    if main_div is not None:
        menu_div = main_div.find_next_sibling('div')
    else:
        print(f"The following restaurant's website was changed and can no longer be scraped.\n\nRestaurant: {restaurant_metadata.name}")
        return None
        
    for id, item in enumerate(menu_div.find_all('li', {'data-test': True}), 0):
        dish_name = item.find('span', {'data-testid': 'rich-text'}).text.strip()
        dish_id = id
        price = item.find('span', {'data-testid': 'rich-text'}).find_next('span').text.strip()
        description = item.find('div', {'class': 'ce gn'})
        description_text = description.text.strip() if description else 'No description'

        menu_item = MenuItems(dish_id, dish_name, description_text, price, restaurant_id)
        menu_items.append(menu_item)
    
    return menu_items

def pretty_print(restaurants: list[VictoriaRestaurants]) -> None:
    """
    Brief: a function to view the restaurant objects in terminal.
    """
    for idx, restaurant in enumerate(restaurants, 1):
        print(f"{idx}. {restaurant}")
        
def pretty_print_menu_items(menu_items: list[MenuItems]) -> None:
    """
    Brief: a function to view the menu objects in terminal
    """
    for idx, menu_item in enumerate(menu_items, 1):
        print(f"{idx}/ {menu_item}")

def main():
    url = BASE_URL + '/ca/city/victoria-bc'
    vic_restaurants = get_restaurant_names_with_menu_urls(url)
    write_restaurants_to_csv(vic_restaurants[0], 'ubereats_restaurants.csv')
    write_menu_items_to_csv(vic_restaurants[1], 'ubereats_restaurant_menu_items.csv')
    # pretty_print(vic_restaurants[0])
    # pretty_print_menu_items(vic_restaurants[1])
    
        
    
if __name__ == "__main__":
    main()