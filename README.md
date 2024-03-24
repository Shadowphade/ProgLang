# ProgLang
## Goals
Compare the following features in go and python
- Concurrancy
- Type System
- Data handleing
- File IO
- Alogrithm Preformance

## Project
The following project is to be implmented in both languages.

The great data shuffle.
Web scraper
    - Each scraper will read in a file called `sites.list` a simple text file with a web site on each line.
    - Some sites will intentionally be dead or fake so errors must be handled.
    - The scraped data is then parsed into sentences and stored as a csv file.
Bin sorting
    - Sorting will try to efficently pack sentences in 100 word bins (preferably concurantly).
    - The bins will then be outputted as another csv.

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
