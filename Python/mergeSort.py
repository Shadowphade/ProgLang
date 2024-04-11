import csv
import threading
import random

class Pokemon:
    name = ""
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

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
