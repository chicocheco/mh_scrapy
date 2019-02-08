## mh_scrapy
Web scraper written in Selenium (Python) inspired by my work in a call center, collecting contact data of rental 
agencies and individuals offering their estates online.
Scraping this sort of data using Scrapy library was successful mostly only with Czech estate websites.

Dependencies:
- `pyenv global 3.7.0; python -m venv venv370; pyenv global system; source venv370/bin/activate`
- `(venv370) pip install scrapy`
- `(venv370) pip install scrapy-fake-useragent`

Procedure:

(0. activate the venv and 'cd' to the project folder):
- `$ source venv370/bin/activate`
- `$ cd mh/mh`

(examples)
**sreality - fully tested**
- open Firefox, get to the search results
- select 20, 40 or 60 results per page
- press CTRL + SHIFT + E to open built-in network monitor of Firefox
- press CTRL + R to reload the page in order to catch the API calls of the website
- copy the Request URL for example: 
`https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=60`
- now, how many pages of results to scrape? let's say 10 pages
- what is going to be the name of the output file? let's say "sreality.csv" (CSV format)
- paste the URL in the `-a spec=` argument, paste the number of pages in the `-a pages=` argument and paste the filename
 in the `-o` argument
- execute the following command with the arguments, example:
`(venv) standa@e330 ~/PycharmProjects/mh/mh $ scrapy crawl sreality -a pages=10 
-a spec='https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=60' -o sreality.csv`

**bezrealitky - tested**
- open Firefox, get to the search results
- copy the URL
- paste the URL in the `-a spec=` argument and paste the filename in the `-o` argument
- execute the following command with the arguments, example:
`(venv) standa@e330 ~/PycharmProjects/mh/mh $ scrapy crawl bezrealitky
 -a spec='https://www.bezrealitky.cz/vypis/nabidka-prodej/byt' -o bezrealitky.csv`

**reality_idnes - not fully tested**
- open Firefox, get to the search results
- copy the URL
- paste the URL in the `-a spec=` argument and paste the filename in the `-o` argument
- execute the following command with the arguments, example:
`(venv) standa@e330 ~/PycharmProjects/mh/mh $ scrapy crawl reality_idnes
 -a spec='https://reality.idnes.cz/s/prodej/byty/' -o reality_idnes.csv`


