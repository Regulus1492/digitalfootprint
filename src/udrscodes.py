import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def main():
    query = '"Juan Carlos Serrano Mera"'
    #Trasnforms query into html readable entry
    query = urllib.parse.quote_plus(query)
    #print(query)

    #Shows if web query was succesful
    response = get_source("https://www.google.com/search?q=" + query)
    print(response)

   





def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


main()