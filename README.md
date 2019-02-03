## mh_scrapy
Web scraper written in Scrapy based on needs of MH Marketing.

How to use the spiders in 'mh' scrapy project:

Dependencies:
- pyenv global 3.7.0; python -m venv venv370; pyenv global system; source venv370/bin/activate
- pip install scrapy
- pip install scrapy-fake-useragent

Procedure:

0. activate the venv and 'cd' to the project folder:
$ source venv370/bin/activate
$ cd mh/mh

(examples)
1. sreality - fully tested
- open Firefox, get to the search results
- select 20, 40 or 60 results per page
- CTRL + SHIFT + E
- CTRL + R
- copy the Request URL: (example: https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=60
- how many pages of results to scrape? let's say 10 pages
- what is going to be the name of the output file? let's say sreality.csv
- paste the URL in the '-a spec=' argument, paste the number of pages in the '-a pages=' argument and paste the filename in the '-o ' argument
- execute the following command with the arguments, example:
(venv) standa@e330 ~/PycharmProjects/mh/mh $ scrapy crawl sreality -a pages=10 -a spec='https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=60' -o sreality.csv

2. bezrealitky - tested enough
- open Firefox, get to the search results
- copy the URL
- paste the URL in the '-a spec=' argument and paste the filename in the '-o ' argument
- execute the following command with the arguments, example:
(venv) standa@e330 ~/PycharmProjects/mh/mh $ scrapy crawl bezrealitky -a spec='https://www.bezrealitky.cz/vypis/nabidka-prodej/byt' -o bezrealitky.csv

3. reality_idnes !!!!!!!! not tested
- open Firefox, get to the search results
- copy the URL
- paste the URL in the '-a spec=' argument and paste the filename in the '-o ' argument
- execute the following command with the arguments, example:
(venv) standa@e330 ~/PycharmProjects/mh/mh $ scrapy crawl reality_idnes -a spec='https://reality.idnes.cz/s/prodej/byty/' -o reality_idnes.csv


