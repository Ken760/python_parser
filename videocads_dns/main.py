import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service


def get_data(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }


def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("general.useragent.override")
    # options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
#
    #Получение страницы с помощью Selenium
    # try:
    #     s = Service("C:/Users/Ken/PycharmProjects/python_parser/driver/chromedriver.exe")
    #     driver = webdriver.Chrome(service=s, options=options)
    #
    #     for i in range(0, 4):
    #
    #         driver.get(f"https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/?p={i}")
    #         sleep(2)
    #
    #         with open(f"index_selenium_{i}.html", "w", encoding='utf-8') as file:
    #             file.write(driver.page_source)
    #
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()

for i in range(0, 4):
    with open(f"index_selenium_{i}.html", encoding='utf-8') as file:
        src = file.read()

        # get video-cards-url
        soup = BeautifulSoup(src, "lxml")

        cards = soup.find_all("a", class_="catalog-product__name")

        for card in cards:
            card = "https://www.dns-shop.ru" + card.get('href')
            print(card)


def main():
    get_data_with_selenium("")


if __name__ == '__main__':
    main()