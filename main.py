from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#for testing purposes
from selenium.webdriver.chrome.options import Options
import pandas as pd
from lxml import etree
import time

from config import user_name, password,chromedriver_location


# Logging in

# For testing, keeping browser open. 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


print(chromedriver_location)


driver = webdriver.Chrome(chrome_options = chrome_options, 
                          service=Service(ChromeDriverManager().install()))

driver.get('https://linkedin.com/uas/login')

time.sleep(5) #waiting for the page to load

username_input = driver.find_element_by_id('username')
username_input.send_keys(user_name)

password_input = driver.find_element_by_id('password')
password_input.send_keys(password)

#click sumbit
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()



# Going to Jobs URL 
jobs_url = 'https://www.linkedin.com/jobs/search/?distance=25.0&f_WT=2&geoId=103644278&keywords=data%20analyst'
driver.get(jobs_url)

#html analysis
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
#using xpath to find the element. 
dom = etree.HTML(soup)

print(soup)
