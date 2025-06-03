import os
import datetime
import random
import json

import requests

url = r"https://spiderbuf.cn/web-scraping-practice/block-ip-proxy"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}


def save_proxies(file):
    if os.path.exists(file):
        return
    get_proxy_url = r"https://proxyfreeonly.com/api/free-proxy-list?limit=500&page=1&sortBy=lastChecked&sortType=desc"
    headers_for_proxies = headers.copy()
    headers_for_proxies.update({"cookie": "_ga=GA1.1.1383985644.1748957778; _ga_SXX6Y4TFQL=GS2.1.s1748957778$o1$g1$t1748957794$j44$l0$h0"})
    response = requests.get(url=get_proxy_url, headers=headers_for_proxies, verify=False)
    with open(file, "w", encoding="utf8") as f:
        f.write(response.json())

def load_proxies(file):
    # # 代理地址和端口
    # proxy = "socks5://username:password@proxy_address:proxy_port"
    with open(file, "r", encoding="utf8") as f:
        data = json.load(f)
        # 解析文件


def get_proxies() -> list[dict]:
    file = f"./{datetime.date.today()}.json"
    # save_proxies(file)
    # data = load_proxies(file)

    return [
        {'http': "socks4://27.77.230.217:1080", 'https': "socks4://181.115.75.102:5678"},
        {'http': "socks4://193.117.138.126:56341", 'https': "socks5://176.236.157.152:8080"},
        {'http': "socks4://124.158.186.34:5678", 'https': "socks4://185.215.53.201:3629"},
    ]


proxies_list = get_proxies()
proxies = random.choice(proxies_list)
print(proxies)
response = requests.get('https://httpbin.org/ip', proxies=proxies)
print(response.text)


# 评价：还是正儿八经整个花钱的代理吧