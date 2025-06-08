import requests
from bs4 import BeautifulSoup, PageElement, Tag, NavigableString

url = r"https://spiderbuf.cn/web-scraping-practice/scraping-scroll-load{page}"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}


# 滚动加载在于服务器返回一个token，客户端拿着token向服务器要数据
def get_token(document: PageElement | Tag | NavigableString):
    page = document.find(attrs={"id": "sLaOuol2SM0iFj4d"})
    if not page:
        return
    return "/" + page.text

page = ""
index = 0
while True:
    response = requests.get(url.format(page=page), headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    for row in soup.find_all("div", {"class": "row"}):
        print(row.get_text(strip=True))
    print()
    if not (page := get_token(soup)):
        break
    elif (index:=index+1) == 5:
        break
