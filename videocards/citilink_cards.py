import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

cards_url_list = []

for i in range(1, 3):
    url = f"https://www.citilink.ru/catalog/videokarty/?p={i}"

    q = requests.get(url)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    cards = soup.find_all(class_='ProductCardHorizontal__title')

    for card in cards:
        card_page_url = "https://www.citilink.ru" + card.get('href')
        cards_url_list.append(card_page_url)

with open(' cards_url_list.txt', 'a') as file:
    for line in cards_url_list:
        file.write(f'{line}\n')