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

def insertionSort(arr, l, h):
    # Implementation of the insertion sort algorithm for a specific range
    for i in range(l + 1, h + 1):
        key = arr[i]
        j = i - 1
        while j >= l and arr[j].price > key.price:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l1, h1, h2):
    # Merge two sorted subarrays into a single sorted array based on price attribute
    count = h2 - l1 + 1
    sorted_arr = [0] * count
    i, k, m = l1, h1 + 1, 0

    while i <= h1 and k <= h2:
        if arr[i].price < arr[k].price:
            sorted_arr[m] = arr[i]
            i += 1
        else:
            sorted_arr[m] = arr[k]
            k += 1
        m += 1

    while i <= h1:
        sorted_arr[m] = arr[i]
        i += 1
        m += 1

    while k <= h2:
        sorted_arr[m] = arr[k]
        k += 1
        m += 1

    arr[l1:l1 + count] = sorted_arr

def mergeSort(arr, l, h):
    length = h - l + 1
    if length <= 5:
        # Using insertion sort for small-sized arrays
        insertionSort(arr, l, h)
        return

    mid = (l + h) // 2

    # Create two threads for sorting the two halves concurrently
    leftThread = threading.Thread(target=mergeSort, args=(arr, l, mid))
    rightThread = threading.Thread(target=mergeSort, args=(arr, mid + 1, h))

    # Start the threads
    leftThread.start()
    rightThread.start()

    # Wait for the threads to finish before merging the sorted halves
    leftThread.join()
    rightThread.join()

    # Merge the sorted subarrays
    merge(arr, l, mid, h)

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

    # sort the pokemon from lowest price to highest price using a concurrent merge sort
    mergeSort(allPokemon, 0, len(allPokemon) - 1)

    # print the sorted pokemon data
    for pokemon in allPokemon:
        print("Name: \t" + pokemon.name + "    \tPrice: \t" + str(pokemon.price))

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

    # sort the pokemon data
    sort()

if __name__ == "__main__":
    main()
