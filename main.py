from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://www.linkedin.com/jobs/search/?distance=25.0&f_WT=2&geoId=103644278&keywords=data%20analyst').text

soup = BeautifulSoup(html_text,'lxml')
job = soup.find('a',id='ember1863')

print(job)
