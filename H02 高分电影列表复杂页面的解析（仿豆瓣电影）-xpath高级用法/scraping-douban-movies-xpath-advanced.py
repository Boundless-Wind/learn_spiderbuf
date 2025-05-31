import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/scraping-douban-movies-xpath-advanced"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

for row in soup.find_all("div",{"class": "row"}):
    print(row.get_text(strip=True))