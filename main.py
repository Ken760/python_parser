from bs4 import BeautifulSoup
import re

with open("blank/index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

# title = soup.h1
# print(title.text)
#
# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)
#
# for item in page_all_h1:
#     print(item)

# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name"}).find("span").text
# print(user_name)


# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)
#
# for item in find_all_spans_in_user_info:
#     print(item)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# next_el = soup.find(class_="post__title").next_element.next_element
# print(next_el)
#
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
# print(post_title)

# links = soup.find(class_="some__links").find_all("a")
# print(links)
#
# for link in links:
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]
#     link_date_attr = link.gett("data_attr")
#     print(link_href_attr)
#     print(link_date_attr)


# find_a_by_text = soup.find("a", text="Одежда")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)
#
# find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_clothes)


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