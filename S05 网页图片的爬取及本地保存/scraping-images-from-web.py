import os
import urllib.parse

import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/scraping-images-from-web"
save_path = r"./img_save"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

parse_url = urllib.parse.urlparse(response.url)
base_url = parse_url.scheme + "://" + parse_url.netloc

if not os.path.exists(save_path):
    os.makedirs(save_path)

for tag_img in soup.find("div", {"class": "table-responsive"}).find_all("img"):
    img_url = urllib.parse.urljoin(base_url, tag_img.get("src"))
    response = requests.get(img_url, headers=headers)

    file_name = tag_img.get("src").rsplit("/",1)[-1]
    with open(os.path.join(save_path, file_name), "wb") as f:
        f.write(response.content)
