import requests
from bs4 import BeautifulSoup
import pandas as pd

# Radaris mining functions

def radaris_search(query):
    page = requests.get(f"https://radaris.com/p{query}")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Get all entries of names
    x = list([text1.get_text() for text1 in soup.find_all('a', class_ = "card-title")])
    # Get Addresses
    y = list([text1.get_text() for text1 in soup.find_all('p', class_ = "res-in")])

    return(list(zip(*[x,y])))
    
    