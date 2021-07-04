import requests
from bs4 import BeautifulSoup
import json
from lxml import *
from lxml.etree import indent

# with open("index.html", encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
#
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get('href')
#
#     all_categories_dict[item_text] = item_href
#
# with open("all_categories_dict.json", "w", encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_categories_dict.json", encoding='utf-8') as file:
    all_categories = json.load(file)

for category_name, category_href in all_categories.items():

    rep = [",", " ", "-"]
    for item in rep:
        if item

