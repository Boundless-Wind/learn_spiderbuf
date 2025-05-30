import base64

import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/scraping-images-base64"

headers = {
    "Referer": "https://spiderbuf.cn/web-scraping-practices/3?order=learn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
tag_img = soup.find("img",{"class": "img-responsive center-block"})
src = tag_img.get("src")[22:]   # data:image/png;base64,实际数据
with open("./img.png", "wb") as f:
    f.write(base64.b64decode(src))