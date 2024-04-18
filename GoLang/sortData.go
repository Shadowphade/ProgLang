package main

import (
	"encoding/csv"
	"log"
	"os"
	"strconv"
	"sync"
)

// func main() {
// 	fmt.Println("Reading csv in")
// 	var prodArr = readIn()
//
// }

func readIn() []PokemonProduct {

	var output []PokemonProduct

	file, err := os.Open("pokemon_data.csv")
	if err != nil { log.Fatal(err) }
	defer file.Close()

	csvReader := csv.NewReader(file)

	records, err := csvReader.ReadAll()
	if err != nil {
		log.Fatal("Parsing CSV failed ", err)
	}


	for _, record := range records {
		if record[0] == "Name" {continue}
		var newPokemon PokemonProduct
		newPokemon.Name = record[0]
		newPokemon.Price = record[1]
		output = append(output, newPokemon)
	}
	return output
}

func sort(inputArr []PokemonProduct, l int, h int) {
	length := h - l + 1

	if length <= 5 {
		// fmt.Println("Length Reached sorting")
		insertionSort(inputArr[l:h+1], length)
		return
	}

	mid := (l + h) / 2

	var wg sync.WaitGroup

	wg.Add(2)

	//fmt.Println("Starting thread")

	go func() {
		defer wg.Done()
		sort(inputArr, l, mid)
	}()
	go func() {
		defer wg.Done()
		sort(inputArr, mid + 1, h)
	}()

	wg.Wait()

	merge(inputArr, l, mid, h)

}

func insertionSort(inputArr []PokemonProduct, sliceSize int) {
	var j int

	for i := 1; i < sliceSize; i++ {

		key := inputArr[i]
		keyVal,err := strconv.ParseFloat(inputArr[i].Price, 64)
		if err != nil {log.Fatal(err)}
		j = i-1;

		check,err := strconv.ParseFloat(inputArr[j].Price, 64)
		if err != nil {log.Fatal(err)}
		for j >= 0 && check > keyVal {
			inputArr[j + 1] = inputArr[j]
			j = j - 1
		}
		inputArr[j+1] = key
	}
	// fmt.Println(inputArr)
}


func merge(arr []PokemonProduct, l1 int, h1 int, h2 int) {
	count := h2 - l1 + 1
	var sorted = make([]PokemonProduct, count)
	i := l1
	k := h1+1
	m := 0

	for (i <= h1 && k <= h2) {
		price1,err := strconv.ParseFloat(arr[i].Price, 64)
		if err != nil {log.Fatal(err)}
		price2,err := strconv.ParseFloat(arr[k].Price, 64)
		if err != nil {log.Fatal(err)}
		if price1 < price2 {
			sorted[m] = arr[i]
			i++
		} else {
			sorted[m] = arr[k]
			k++
		}
		m++
	}

	for i <= h1 {
		sorted[m] = arr[i]
		m++
		i++
	}
	for k <= h2 {
		sorted[m] = arr[k]
		m++
		k++
	}
	//arrCount := l1
	for i := 0; i < count; i,l1 = i+1, l1 + 1{
		arr[l1] = sorted[i]
	}

}
