from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from tqdm import tqdm
import requests
from datetime import date
import csv

BASE_URL = 'https://www.ubereats.com'

class MenuItems:
    def __init__(self, restaurant, name, description, price):
        self.restaurant = restaurant
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"Dish name: {clean_text(self.name)}\nDish price:{self.price}\nRestaurant:{clean_text(self.restaurant)}\nDescription:{clean_text(self.description)}"

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

def get_restaurant_names_with_menu_urls(url: str) -> list[VictoriaRestaurants]:
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
    url_index = 0
    descriptions_and_addresses = soup.findAll('span')

    print(len(descriptions_and_addresses))
    descriptions_and_addresses_index = 0
    
    for i, restaurant in enumerate(soup.findAll('h3'), 0):
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
        restaurants.append(restaurant)
        url_index += 1
        print(descriptions_and_addresses_index)
        
    return restaurants


def extract_menu_items(restaurants_metadata: list[VictoriaRestaurants]):
    menu_items = []
    for restaurant in tqdm(restaurants_metadata):
        url = BASE_URL + restaurant.menu_page_url
        restaurant_name = restaurant.name
        
        response = requests.get(url)
        
        if response.status_code != 200:
            raise Exception(f"Failed to load page {url}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Finding the div with the desired menu items
        main_div = soup.find('div', {'id': 'store-desktop-menu-nav'})
        
        # The div with menu items is directly after a div with id "store-dektop-menu-nav". How convenient!
        if main_div is not None:
            menu_div = main_div.find_next_sibling('div')
        
        for item in menu_div.find_all('li', {'data-test': True}):
            dish_name = item.find('span', {'data-testid': 'rich-text'}).text.strip()
            price = item.find('span', {'data-testid': 'rich-text'}).find_next('span').text.strip()
            description = item.find('div', {'class': 'ce gn'}) # this class might be wrong
            description_text = description.text.strip() if description else 'No description'
            
            menu_item = MenuItems(restaurant_name, dish_name, description_text, price)
            menu_items.append(menu_item)
            # print(menu_item)
    
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
    write_restaurants_to_csv(vic_restaurants, 'ubereats_restaurants.csv')
    pretty_print(vic_restaurants)
    menu_items = extract_menu_items(vic_restaurants)
    print(len(menu_items))
    pretty_print_menu_items(menu_items)
    
        
    
if __name__ == "__main__":
    main()