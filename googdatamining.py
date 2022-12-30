#Web scrapping google searches
#Source
# https://practicaldatascience.co.uk/data-science/how-to-scrape-google-search-results-using-python
# https://blog.tdstelecom.com/security/how-to-search-and-find-your-digital-footprint/
# Not checked, pending
# chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://repositorio.cepal.org/bitstream/handle/11362/45484/4/S2000380_en.pdf

import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession


def main():
    # query = '"Juan Carlos Serrano Mera"'
    # query = urllib.parse.quote_plus(query)
    # response = get_source("https://www.google.com/search?q=" + query)
    # links = list(response.html.absolute_links)
    # google_domains = ('https://www.google.', 
    #                   'https://google.', 
    #                   'https://webcache.googleusercontent.', 
    #                   'http://webcache.googleusercontent.', 
    #                   'https://policies.google.',
    #                   'https://support.google.',
    #                   'https://maps.google.')

    # for url in links[:]:
    #     if url.startswith(google_domains):
    #         links.remove(url)

    #print(links)

    query = '"Juan Carlos Serrano Mera"'
    results = google_search(query)
    print(results)
    

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
    
    
def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    
    return response

def parse_results(response):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:

        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': result.find(css_identifier_text, first=True).text
        }
        
        output.append(item)
        
    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)


main()