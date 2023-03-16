from selenium import webdriver
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

data = pd.DataFrame(columns=['text', 'rating'])
row = {'text': 'zz', 'rating': 5}
#data = data.append(row, ignore_index=True)
#print(data)


connection_driver = webdriver.Chrome(ChromeDriverManager().install())
connection_driver.get('https://www.metacritic.com/browse/games/release-date/available/pc/metascore?page=0')
connection_driver.maximize_window()
time.sleep(4)

games = connection_driver.find_elements(By.CLASS_NAME, 'clamp-image-wrap')

for game in games:
    time.sleep(4)
    game.click()

    time.sleep(4)
    reviews = connection_driver.find_elements(By.CLASS_NAME, 'module_title')
    reviews[3].click()

    time.sleep(4)
    html_source = connection_driver.page_source
    page_soup = soup(html_source, 'html.parser')
    review_divs = page_soup.findAll('div', {'class': lambda value: value and value.startswith('review_section')})

    print(review_divs[0])