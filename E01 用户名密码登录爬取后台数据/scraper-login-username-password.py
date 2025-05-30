import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

# 1. 利用session会话管理，自动处理cookie
url = r"https://spiderbuf.cn/web-scraping-practice/scraper-login-username-password/login"
data = {
    "username": "admin",
    "password": "123456",
}
with requests.Session() as session:
    response = session.post(url, headers=headers, data=data)
    soup = BeautifulSoup(response.text, "lxml")
    print(soup.prettify())

# 2. 利用cookie直接访问登录后页面
url = r"https://spiderbuf.cn/web-scraping-practice/scraper-login-username-password/list"
cookie = {"admin": "b8628f1b3925d448a015926883cb941f"}
response = requests.get(url, headers=headers, cookies=cookie)
print(response.request.headers)
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())
