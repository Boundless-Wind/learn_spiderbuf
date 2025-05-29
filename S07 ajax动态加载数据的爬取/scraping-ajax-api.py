import requests
import json

# url = r"https://spiderbuf.cn/web-scraping-practice/scraping-ajax-api"
url = r"https://spiderbuf.cn/web-scraping-practice/iplist"
headers = {
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://spiderbuf.cn/web-scraping-practice/scraping-ajax-api",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

response = requests.get(url, headers=headers)
print(response.encoding)
print(response.json())  # requests的自动猜解猜错了
print(json.loads(response.content))

response.encoding = "utf-8" # 手动指定即可
print(response.encoding)
print(response.json())
print(json.loads(response.content))