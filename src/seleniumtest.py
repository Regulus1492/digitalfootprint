from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), executable_path='C:\Users\jserrano\Downloads\chromedriver.exe')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=Service(executable_path = "C:\\browserdrivers\\chromedriver.exe"))
    driver.get("https://www.google.com")
    

main()


# Posible help
# https://www.selenium.dev/selenium/docs/api/py/api.html
# https://selenium-python.readthedocs.io/api.html
# Too old
# https://stackoverflow.com/questions/49323099/webdriverexception-message-service-chromedriver-unexpectedly-exited-status-co
# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver
# executable path not working any more
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
# Chrome drivers pages
# https://sites.google.com/chromium.org/driver/?pli=1

