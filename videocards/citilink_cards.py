import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import pandas
from urllib.parse import urljoin

# cards_url_list = []
#
# for i in range(1, 3):
#     url = f"https://www.citilink.ru/catalog/videokarty/?p={i}"
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result, 'lxml')
#     cards = soup.find_all(class_='ProductCardHorizontal__title')
#
#     for card in cards:
#         card_page_url = "https://www.citilink.ru" + card.get('href')
#         cards_url_list.append(card_page_url)
#
# with open('cards_url_list.txt', 'a') as file:
#     for line in cards_url_list:
#         file.write(f'{line}\n')
#
# with open('cards_url_list.txt') as file:
#     lines = [line.strip() for line in file.readlines()]
#
#     for line in lines:
#         q = requests.get(line)
#         result = q.content
#
#         soup = BeautifulSoup(result, 'lxml')
#         # cards = soup.find(class_=)

# Тестирование
# q = requests.get('https://www.citilink.ru/product/videokarta-palit-nvidia-geforce-rtx-3060-pa-rtx3060-dual-12g-12gb-gddr-1469005/')
# result = q.content
#
# soup = BeautifulSoup(result, 'lxml')
# title = soup.find(class_="ProductCardLayout__product-description").find('h1').text
# price = soup.find(class_="ProductPrice__price ProductHeader__price-default__price").text
# card_name = title.strip().split(',')
# name = card_name[0]
# card_price = ' '.join(price.split())
#
# print(name)
# print(f"Цена: {card_price}")

#
with open('cards_url_list.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        title = soup.find(class_="ProductCardLayout__product-description").find('h1').text
        try:
            price = soup.find(class_="ProductPrice__price ProductHeader__price-default__price").text
            card_name = title.strip().split(',')
            name = card_name[0]
            card_price = ' '.join(price.split())
        except:
            print("Нет в наличии")

        data = {
            'name': name,
            'price': card_price,
        }
        count += 1
        sleep(3)
        print(f'#{count}: {line} is done!')

        data_dict.append(data)

        with open('data.json', 'w',  encoding="utf-8") as json_file:
            json.dump(data_dict, json_file, indent=4, ensure_ascii=False,)

pandas.read_json()
print(pandas)