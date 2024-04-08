import requests
from bs4 import BeautifulSoup
import csv
import time
import threading
import random

class Pokemon:
    name = ""
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price


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

def sort():
    # collect data from .csv file (names and prices as key value pairs in a dictionary)
    pokemonDict = createDictionaryFromCsv()

    # create array of pokemon data containers using the dictionary
    allPokemon = [0 for i in range (len(pokemonDict))]
    counter = 0
    for i,j in pokemonDict.items():
        tempPokemon = Pokemon(i, j)
        allPokemon[counter] = tempPokemon
        counter += 1

def createDictionaryFromCsv():
    pokemonDict = {}

    file = open("pokemon_prices.csv", "r")
    data = csv.reader(file)

    for row in data:
        name = row[0]
        price = float(row[1])
        pokemonDict[name] = price

    return pokemonDict

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
    sort()
