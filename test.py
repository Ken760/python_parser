import requests
from bs4 import BeautifulSoup

# url = "https://health-diet.ru/table_calorie/"
# # url = "http://80.78.245.207:8000/"
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 "
#                   "Safari/537.36"
# }
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open("index.html", "w", encoding='utf-8') as file:
#     file.write(src)

with open("index.html", encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

for item in all_products_hrefs:
    item_text = item.text
    item_href = "https://health-diet.ru" + item.get('href')
    print(f"{item_text}:{item_href}")
