import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/requests-lxml-for-scraping-beginner"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())
