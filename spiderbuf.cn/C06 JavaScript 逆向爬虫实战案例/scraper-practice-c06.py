from hashlib import md5
from random import random
from time import time

import requests
from bs4 import BeautifulSoup


# 在发包时打断点，对于混淆的数据放在控制台上即可推断出是什么东西
def getPageData():
    random_num = int(random() * 0x1f40 + 0x7d0)  # 生成随机数
    timestamp = int(time())  # 计算秒级时间戳
    signture = md5(f"{random_num}spiderbuf{timestamp}".encode()).hexdigest()  # 生成MD5哈希值
    # 构建返回数据
    return {
        "random": random_num,
        "timestamp": timestamp,
        "signture": signture
    }


# print(getPageData())

url = r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c06"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "cookie": "_asd2sdf99=gvGAJJbfZxDhI17Eu59KPhAkT1nzJ6zM"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

total = 0

for item in soup.find("div", {"id": "items"}).find_all("div", recursive=False):
    total += float(item.find("span").find_next_sibling("span").text)

response = requests.post(url, json=getPageData(), headers=headers)

for item in response.json():
    total += float(item.get("rating"))

print(round(total, 2))
