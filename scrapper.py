import time
import pandas as pd
import re
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from langdetect import detect
from datetime import datetime

connection_driver = webdriver.Chrome(ChromeDriverManager().install())

# loop for number of game pages

for i in range(70):
    data = pd.DataFrame(columns=['text', 'rating'])
    hrefs = []

    connection_driver.get('https://www.metacritic.com/browse/games/release-date/available/pc/metascore?page=' + str(i))
    time.sleep(3)

    html_source = connection_driver.page_source
    page_soup = soup(html_source, 'html.parser')
    href_divs = page_soup.findAll('td', {'class': 'clamp-image-wrap'})

    # loop for scanning href to games on actual game page

    for div in href_divs:
        div = str(div)
        start_href = 'a href='
        end_href = '"><img'
        href_start = div.index(start_href)
        href_end = div.index(end_href)
        href = div[href_start + len(start_href) + 1: href_end]
        hrefs.append(href)

    # loop for each game in games on actual page

    for href in hrefs:
        print(f'Page number: {i}, Game: {href[9:]}, Number the game on page: {hrefs.index(href)} \n'
              f'Already {len(data)} comments stored\n')

        # opens a page with comments for game

        connection_driver.get('https://www.metacritic.com' + href + '/user-reviews')
        actual_page_number = 0
        time.sleep(2)

        # check number of pages for comments

        html_source = connection_driver.page_source
        page_soup = soup(html_source, 'html.parser')
        if page_soup.find('li', {'class': 'page last_page'}):
            last_page_div = str(page_soup.find('li', {'class': 'page last_page'}))
            last_page_searching_end = '</a></li>'
            end = last_page_div.index(last_page_searching_end)
            last_page_number = int(last_page_div[end - 1: end])
        else:
            last_page_number = 1

        # loop each comment page number

        for actual_page_number in range(last_page_number):
            if actual_page_number != 0:
                connection_driver.get(
                    'https://www.metacritic.com' + href + '/user-reviews?page=' + str(actual_page_number))

            html_source = connection_driver.page_source
            page_soup = soup(html_source, 'html.parser')
            review_divs = page_soup.findAll('div', {'class': 'review_content'})

            for user_review in review_divs:
                rating_div = str(user_review.find('div', {'class': 'review_grade'}))
                text_div = str(user_review.find('div', {'class': 'review_body'}))

                rating_searching_start = '">'
                rating_searching_end = '<'
                rating_start = rating_div.index(rating_searching_start, 50)
                rating_end = rating_div.index(rating_searching_end, rating_start)
                rating = rating_div[rating_start + len(rating_searching_start): rating_end]

                text_searching_start = '<span>'
                text_searching_end = '</span>'
                try:
                    text_start = text_div.index(text_searching_start)
                except:
                    try:
                        text_searching_start = '<span class="blurb blurb_expanded">'
                        text_start = text_div.index(text_searching_start)
                    except:
                        continue
                text_end = text_div.index(text_searching_end, text_start)
                text = text_div[text_start + len(text_searching_start): text_end]
                text = re.sub(r'<.*?>', '', text)
                text = text.replace('\n', ' ')

                # check if comment is written in english

                try:
                    if detect(text) != 'en':
                        continue
                except:
                    continue

                row = {'rating': rating, 'text': text}
                data = data.append(row, ignore_index=True)
        time_start = datetime.now()
        data.to_csv('data_page' + str(i) + '.csv')
        time_end = datetime.now()
        print(f'Csv creating time: {time_end - time_start}')