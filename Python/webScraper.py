import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_page(page_number):
    url = f"https://scrapeme.live/shop/page/{page_number}/"
    response = requests.get(url)
    if response.status_code == 404:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    pokemon_data = []
    for product in soup.find_all("li", class_="product"):
        name = product.find("h2", class_="woocommerce-loop-product__title").text
        price = product.find("span", class_="woocommerce-Price-amount amount").text.replace('£', '')
        pokemon_data.append({"pokemon": name, "price": price})
    return pokemon_data

def main():
    start_time = time.time()
    filename = "pokemon_prices.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['pokemon', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        page_number = 1
        while True:
            pokemon_data = scrape_page(page_number)
            if pokemon_data is None:
                break
            for data in pokemon_data:
                writer.writerow(data)
            print(f"Data from page {page_number} written to CSV.")
            page_number += 1

    end_time = time.time()
    print(f"Scraping complete in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()