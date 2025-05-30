import time

import requests

url = r"https://spiderbuf.cn/web-scraping-practice/scraper-bypass-request-limit/{page_num}"

headers = {
    "Referer": "https://spiderbuf.cn/web-scraping-practices/3?order=learn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

for i in range(1, 21):
    response = requests.get(url.format(page_num=i), headers=headers)
    print(response.text)
    time.sleep(1)   # 延迟一会