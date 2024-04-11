package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strings"
    // api for web scrapping
	//"sync"
	"github.com/gocolly/colly"
)

type PokemonProduct struct {
	Name  string
	Price string
}

func main() {
	// initialize the slice to store scraped data
	var pokemonProducts []PokemonProduct

	// create a new collector instance
	c := colly.NewCollector()

	// define the URL pattern for pagination
	baseURL := "https://scrapeme.live/shop/page/%d/"
	lastPage := 48

	argLen := len(os.Args[1:])

	if argLen == 0 {
		fmt.Println("Starting Scraper...")

		// define the callback to extract data from each product
		c.OnHTML("li.product", func(e *colly.HTMLElement) {
			// extract Pokemon name and price
			name := e.ChildText("h2")
			price := e.ChildText(".price")

			// eemove pound sign from price
			price = strings.TrimLeft(price, "£")

			// append the data to the slice
			pokemonProducts = append(pokemonProducts, PokemonProduct{Name: name, Price: price})
		})

		for i := 1; i <= lastPage; i++ {
			url := fmt.Sprintf(baseURL, i)

			c.Visit(url)
		}

		// write the scraped data to a CSV file
		err := writeCSV("pokemon_data.csv", pokemonProducts)
		if err != nil {
			log.Fatalf("Error writing CSV file: %v", err)
		}

		fmt.Println("Scraping and CSV generation completed successfully.")
	}



	fmt.Println("Starting Sorting... ")

	products := readIn()
	// var wg sync.WaitGroup
	sort(products, 0, len(products) - 1)
	writeCSV("sorted.csv", products)
	fmt.Println(products)
}

func writeCSV(filename string, data []PokemonProduct) error {
	// create or open the CSV file
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	// create a CSV writer
	writer := csv.NewWriter(file)
	defer writer.Flush()

	// write CSV headers
	err = writer.Write([]string{"Name", "Price"})
	if err != nil {
		return err
	}

	// write data to the CSV file
	for _, p := range data {
		err := writer.Write([]string{p.Name, p.Price})
		if err != nil {
			return err
		}
	}

	return nil
}
