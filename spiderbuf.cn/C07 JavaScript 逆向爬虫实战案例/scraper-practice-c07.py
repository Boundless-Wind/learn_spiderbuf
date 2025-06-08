from hashlib import md5
from random import random
from time import time

import requests
from bs4 import BeautifulSoup


def get_payload(token):
    timestamp = int(time())  # 计算秒级时间戳
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    key = ''.join([characters[int(random() * len(characters))] for _ in range(32)])
    # 构建返回数据
    return {
        "key": key,
        "timestamp": timestamp,
        "token": token,
    }


def set_cookie(payload):
    _md5 = md5(f"{payload['timestamp']}{payload['token']}{payload['key']}".encode()).hexdigest()
    cookie = '_asd2sdf99=' + _md5 + '; path=/;'
    headers.update({"cookie": cookie})



url = r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c07"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "cookie": "_asd2sdf99=656d2bed38266a468690a4c17675ce38"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("input", attrs={"name": "token"})["value"]

payload = get_payload(token)
# 这道题会在设置data时设置cookie，所以两者必须同步修改
# 正常cookie是服务端响应 set-cookie ，这题是浏览器js设置
set_cookie(payload)
response = requests.post(url, json=payload, headers=headers)

cpc_total = 0
cpc_num = 0

# 位运算优先级较低，所以加个括号
for item in response.json():
    cpc_total += (item.get("cpc_usd") ^ item.get('monthly_search_volume')) / 0x64
    cpc_num += 1

print(round(cpc_total / cpc_num, 2))
