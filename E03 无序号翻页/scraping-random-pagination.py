import urllib.parse

import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/scraping-random-pagination"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

parse_url = urllib.parse.urlparse(response.url)
base_url = parse_url.scheme + "://" + parse_url.netloc

for tag_a in soup.find("ul", {"class": "pagination"}).find_all("a"):
    page_link = urllib.parse.urljoin(base_url, tag_a["href"])
    print(page_link)
