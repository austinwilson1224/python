from os import path
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager


# virtual web browser
driver = webdriver.Chrome(ChromeDriverManager().install())


# the structure of this site is hard to parse need to use xpath
url = "https://www.net-a-porter.com/en-us/"
driver.get(url)
url = "https://www.net-a-porter.com/en-us/shop/product/piaget/limelight-gala-26mm-18-karat-rose-gold-and-diamond-watch/1320652"
url = "https://www.nordstrom.com/s/ugg-scuff-slipper-men/5704734?origin=category-personalizedsort&breadcrumb=Home%2FMen%2FShoes%2FComfort&color=black%20suede"
# creating a webdriver (instance of google chrome -- not gonna work with safari)


price = float(driver.find_element_by_id("current-price-string").text.strip("$"))
price



















######## OTHER SHIT THAT MAY NOT BE RELEVANT #############
##
###
####
#####
######
#######
########            no one cares VVVVVVV
# too see if the file already exists 
url_file_exist = path.isfile("shopping_sites.csv")


if not url_file_exist:
    # create a new file based on user input
    df = pd.DataFrame()
    # df.columns = ["url"]
    df.to_csv("shopping_sites.csv")
    pass






# functions 