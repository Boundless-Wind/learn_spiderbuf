import requests

url = r"https://spiderbuf.cn/web-scraping-practice/user-agent-referrer"

headers = {
    "Referer": "https://spiderbuf.cn/web-scraping-practices/3?order=learn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

# Referrer是来源的标识，关于少一个r是因为标准写错了（草台班子）

response = requests.get(url, headers=headers)
print(response.text)