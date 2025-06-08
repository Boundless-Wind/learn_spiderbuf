import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

# 面对验证码的几种处理方法
# 1. 登陆后cookie：麻烦
url = r"https://spiderbuf.cn/web-scraping-practice/web-scraping-with-captcha/list"
cookie = {"admin": "b8628f1b3925d448a015926883cb941f"}
response = requests.get(url, headers=headers, cookies=cookie)
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

# 2. 打码平台：要钱
# 3. OCR：错误率稍高
