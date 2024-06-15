from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class VictoriaRestaurants:
    def __init__(self, name, menu_page_url):
        self.name = name
        self.menu_page_url = menu_page_url
        
    def __str__(self):
        return f"{clean_text(self.name)}: {clean_text(self.menu_page_url)}"

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
    
    for x in soup.findAll('h3'):
        if x.text.endswith('?'):
            continue
        clean_name = clean_text(x.text)
        restaurant = VictoriaRestaurants(clean_name, menu_urls[url_index])
        restaurants.append(restaurant)
        url_index += 1
        
    return restaurants

def pretty_print(restaurants: list[VictoriaRestaurants]) -> None:
    """
    Brief: a function to view the restaurant objects in terminal.
    """
    for idx, restaurant in enumerate(restaurants, 1):
        print(f"{idx}. {restaurant}")

def main():
    url = "https://www.ubereats.com/ca/city/victoria-bc"
    vic_restaurants = get_restaurant_names_with_menu_urls(url)
    pretty_print(vic_restaurants)
        
    
if __name__ == "__main__":
    main()