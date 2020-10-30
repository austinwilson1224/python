import urllib.request
from urllib import request
import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets"
url2 = "https://www.blowoutcards.com/sports-cards/basketball-cards/2020-21/2020-21-panini-contenders-draft-picks-basketball-hobby-12-box-case.html"



t = requests.get(url2)


test_url = "https://www.blowoutcards.com"
test2 = request.urlopen(test_url).read()
soup2 = BeautifulSoup(test2, "lxml")
soup2
price = soup2.findAll("div")
price


test = request.urlopen(url2).read()

soup = BeautifulSoup(test, "html.parser")

soup


# mydivs = soup.findAll("div", {"class": "stylelistrow"})

price = soup.findAll("div", {"class": "price"})
price


# soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

# tbody = soup('table', {"class": "wikitable plainrowheaders sortable "})[0].find_all("tr")

# for row in tbody:
#     cols = row.findChildren(recursive = False)
#     print(cols)