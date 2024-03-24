# ProgLang
## Goals
Compare the following features in Go and Python
- Concurrency
- Type System
- Data handling
- File IO
- Algorithm Performance

## Project- The Great Data Shuffle
The following project is to be implemented in both languages.

Web Scraper<br>
- Each scraper will read in a file called `sites.list` a simple text file with a website on each line.
  - Likely 100 wikipedia links
- Some sites will intentionally be dead or fake so errors must be handled.
  - 10 fake/dead links of the 100 total links
- The scraped data is then parsed into sentences and stored as a csv file.
  - Store all scraped data in one file or the first sentence of each site into one file??

Bin Sorting<br>
- Concurrently pack sentences in 100-word bins.
  - Run 3 cases: 1 goroutine/thread, 4 goroutines/threads, 8 goroutines/threads
- The bins will then be outputted as another csv.
  - Each line in the CSV will have a 100-word 'sentence' (aka the info of one bin)

## Language Notes

### Golang
Includes:
- net/http : standard http networking library
- bufio : handles IO with files
- os : allows for interaction with os syscalls
- bytes : encoding and decoding of data

### Python
Includes:
- requests : handles http requests
