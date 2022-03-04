import csv

import requests
import os
from bs4 import BeautifulSoup
from time import sleep
import json
from datetime import datetime


def get_all_pages():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    }

    # r = requests.get(url="https://www.citilink.ru/catalog/smartfony/?sorting=price_asc&f=discount.any%2Crating.any", headers=headers)
    #
    # if not os.path.exists("data"):
    #     os.mkdir("data")
    #
    # with open("data/page_el.html", "w", encoding='utf-8') as file:
    #     file.write(r.text)

    with open("data/page_el.html", encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    pages_count = int(soup.find("div", class_="ProductCardCategoryList__pagination").find_all("a")[-2].text)

    for i in range(1, pages_count + 1):
        url = f"https://www.citilink.ru/catalog/smartfony/?f=discount.any%2Crating.any&sorting=price_desc&p={i}"
        print(url)

    #     r = requests.get(url=url, headers=headers)
    #
    #     with open(f"data/page_{i}.html", "w", encoding='utf-8') as file:
    #         file.write(r.text)
    #
    #     sleep(2)
    #
    # return pages_count + 1


def main():
    get_all_pages()


if __name__ == '__main__':
    main()
