import requests
from bs4 import BeautifulSoup

for i in range(0, 8):
    url = f"https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/?p={i}"
    print(url)
