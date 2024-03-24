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
- Each scraper will read https://scrapeme.live/shop/page/4/
    - Data will consist of the pokemon and their price.
- The scraped data is then parsed into sentences and stored as a csv file.
  - Store all scraped data in one file or the first sentence of each site into one file??

Bin Sorting<br>
- A form of concurrant merge sort will be used to sort the pokemon by price.
  -  A csv will be recorded sorted by price.

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
-
