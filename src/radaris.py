import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    #query = '"Patricia Mera"'
    #query = urllib.parse.quote_plus(query)
    query = "/Patricia/Mera/"
    response = get_source(f"https://radaris.com/p{query}")
    links = list(response.html.absolute_links)
    #print(links)

    # css_identifier_result = ".align-items-baseline , .age , .card-title , strong:nth-child(1)"
    css_identifier_result = ".card-title" #si solo uso este puedo sacar el nombre. 
    # css_identifier_result = ".d-flex div div :nth-child(1)" #Salen resultados como nombres de familia relacionada
    #  css_identifier_result = ".align-items-baseline , .btn-primary , .card-title , strong:nth-child(1)"
    #css_identifier_result = ".age"
  
    ccs_idnetifier_name = "Element"
    #Encuentra el objeto css segun su nombre. Con eso puedo hacer el mineo necesario. Pero entender que elementos necesito. 
    results = response.html.find(css_identifier_result)
    
    output1 = []
    for result in results:

        item = {
            'name' : result.attrs['href']
        }

        output1.append(item)
    
    print(output1)

    # for result in results:
    #     print(result)
        
    
    
    # for result in results:

    #     item = {
    #         'name': result.find(ccs_idnetifier_name, first=True).text
    #     }
        
    #     output1.append(item)
        
    # print(output1)

    # Selenium
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    # time.sleep(8)

    # url = "https://radaris.com/p/Patricia/Mera/"
    # driver.get(url)
    # time.sleep(5)

    # soup = BeautifulSoup(driver.page_source, 'lxml')
    # var2 = soup.find('span',{'class':'d-flex'}).text
    # print(var2)
    #driver.quit()

    # browser = webdriver.Firefox()

    # browser.get('http://www.yahoo.com')
    # assert 'Yahoo' in browser.title

    # elem = browser.find_element(By.NAME, 'p')  # Find the search box
    # elem.send_keys('seleniumhq' + Keys.RETURN)

    # browser.quit()





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



#Notes 
# Tried this: 
# Selenium is not working apparenty. Selenium helps to retrieve data when content is dynamic. 
# https://stackoverflow.com/questions/70203783/unable-to-access-span-class-while-web-scraping-using-beautifulsoup
# https://www.selenium.dev/selenium/docs/api/py/