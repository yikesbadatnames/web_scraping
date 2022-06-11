from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

from config import user_name, password,chromedriver_location

print(chromedriver_location)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://linkedin.com/uas/login')

#waiting for the page to load
time.sleep(5)

print(user_name)
