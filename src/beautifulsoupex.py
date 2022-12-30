#Beautiful soup example

import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    page = requests.get("https://radaris.com/p/Patricia/Mera/")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Get all entries of names
    x = list([text1.get_text() for text1 in soup.find_all('a', class_ = "card-title")])
    # Get Addresses
    y = list([text1.get_text() for text1 in soup.find_all('p', class_ = "res-in")])

    for item in zip(*[x,y]):
        print(item)
    

    

    #Get text
    # print(soup.get_text())



main()


# Source
# https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
