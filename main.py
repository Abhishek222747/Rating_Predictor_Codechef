import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from csv_writer import put_data

driver = webdriver.Chrome('./chromedriver')
data = []
for _ in range(132):

    page = randint(1, 279)

    url = """https://www.codechef.com/rankings/COOK133C?order=asc&page=""" + str(page) + """&sortBy=rank"""
    driver.get(url)
    html = driver.page_source

    # got to find text in <div id="ember388" class="ember-view">
    soup = BeautifulSoup(html, "html.parser")

    soup = soup.find('center')
    soup = soup.find('center')
    soup = soup.find('table', class_="dataTable")
    soup = soup.find('tbody')

    arr = soup.find_all('tr')

    for i in range(min(len(arr), 2)):

        users = arr[randint(0, len(arr) - 1)]

        try:
            user_url = "https://www.codechef.com" + users.find('a').get('href')
            driver.get(user_url)
            profile_html = driver.page_source
            profile_soup = BeautifulSoup(profile_html, "html.parser")

            profile_soup = profile_soup.find('div', class_='rank-stats')
            rank = users.find('div').get_text()
            rating, change = map(str, (profile_soup.find('a').get_text()).split())
            change = int(change[1:-1])
            rating = int(rating) - change

            # print("->Rank:", users.find('div').get_text(), "  ->Rating:", rating, "  ->Delta:", change)
            # appending percentile rank to each candidate
            data.append([int(rank)/6953, rating, change])

        except AttributeError:
            pass

driver.close()
put_data(data=data)
