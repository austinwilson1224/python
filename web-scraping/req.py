import requests
from bs4 import BeautifulSoup
import csv

src = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)').text

src2 = requests.get('https://www.blowoutcards.com/sports-cards/basketball-cards/2020-21/2020-21-panini-contenders-draft-picks-basketball-hobby-12-box-case.html').text


src3 = requests.get('https://www.google.com').text

src4 = requests.get('https://www.blowoutcards.com/2018-topps-wwe-wrestling-hanger-pack-12-box-lot.html').text

soup = BeautifulSoup(src, 'lxml')
soup2 = BeautifulSoup(src2, 'lxml')
soup3 = BeautifulSoup(src3, 'lxml')
soup4 = BeautifulSoup(src4, 'lxml')
soup4


csv_file = open('test.csv', 'w')
csv_writer = csv.writer(csv_file)


table = soup.find_all('table','wikitable')

len(table)

table[1]

# looking for class wikitable

