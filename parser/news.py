from pprint import pprint

import requests
from bs4 import BeautifulSoup


URL = "https://kaktus.media/?lable=8&date=2023-04-01&order=time"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    themes = soup.find_all('div', class_="Tag--article")
    news = []

    for item in themes:
        post = {
            "title": item.find("a", class_="ArticleItem--name").string,
            "url": item.find("a", class_="ArticleItem--name").get("href")
        }
        news.append(post)
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        return get_data(html.text)



