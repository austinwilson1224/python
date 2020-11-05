import requests
from bs4 import BeautifulSoup
import csv

src = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)').text

soup = BeautifulSoup(src, 'lxml')

csv_file = open('test.csv', 'w')
csv_writer = csv.writer(csv_file)


table = soup.find_all('table','wikitable')

len(table)

table[1]

# looking for class wikitable

