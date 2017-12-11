from bs4 import BeautifulSoup

import requests

source = requests.get('https://raw.githubusercontent.com/ThaWeatherman/scrapers/master/boardgamegeek/games.csv').text

soup = BeautifulSoup(source, 'lxml')


article = soup.find('article')

print(article)
