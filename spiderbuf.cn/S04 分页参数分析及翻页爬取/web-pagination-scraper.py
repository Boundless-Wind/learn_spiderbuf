import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/web-pagination-scraper"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

for tag_a in soup.find("ul",{"class":"pagination"}).find_all("a"):
    response = requests.get(url, params=tag_a.get("href"), headers=headers)
    print(response.url)