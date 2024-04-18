package main

import (
	"encoding/csv"
	"log"
	"os"
	"strconv"
	"sync"
	//"fmt"
)

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
		//fmt.Println("Length Reached sorting")
		insertionSort(inputArr[l:h+1], length)
		return
	}

	mid := (l + h) / 2
	var wg sync.WaitGroup

	wg.Add(2)

	go func() {
		defer wg.Done()
		sort(inputArr[:], l, mid)
	}()
	go func() {
		defer wg.Done()
		sort(inputArr[:], mid + 1, h)
	}()

	wg.Wait()

	merge(inputArr[:], l, mid, h)

}

func insertionSort(inputArr []PokemonProduct, sliceSize int) {
	var j int

	for i := 1; i < sliceSize; i++ {
		j = i
		for j > 0 {
			keyVal,_ := strconv.ParseFloat(inputArr[j-1].Price, 64)
			check,_ := strconv.ParseFloat(inputArr[j].Price, 64)
			if(check > keyVal){
				 inputArr[j], inputArr[j - 1] = inputArr[j - 1], inputArr[j]
			}
			j = j - 1
		}
	}

	for i, j := 0, sliceSize - 1; i < j; i, j = i+1, j-1 {
		inputArr[i], inputArr[j] = inputArr[j], inputArr[i]
	}
}


func merge(arr []PokemonProduct, l1 int, h1 int, h2 int) {
	count := h2 - l1 + 1
	var sorted = make([]PokemonProduct, count)
	i := l1
	k := h1+1
	m := 0

	for i <= h1 && k <= h2 {
		price1,err := strconv.ParseFloat(arr[i].Price, 64)
		//fmt.Println("Price1:", price1)
		if err != nil {log.Fatal(err)}
		price2,err := strconv.ParseFloat(arr[k].Price, 64)
		//fmt.Println("Price2:", price2)
		if err != nil {log.Fatal(err)}

		if price1 < price2 {
			sorted[m] = arr[i]
			i++
		} else if (price2 < price1) {
			sorted[m] = arr[k];
			k++
		} else if (price1 == price2){
			sorted[m] = arr[i]
			m++
			sorted[m] = arr[k];
			i++
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
	for i := 0; i < count; i++{
		arr[l1] = sorted[i]
		//fmt.Println(sorted[i])
		l1++
	}

}
