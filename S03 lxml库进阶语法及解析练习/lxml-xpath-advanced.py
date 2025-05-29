import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/lxml-xpath-advanced"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

tr_tags = soup.find("table", attrs={"class": "table"}).find("tbody").find_all("tr")
for tr in tr_tags:
    # 只查找一层，所以不需要递归
    tds = tr.find_all("td", recursive=False)
    if not tds:
        continue
    last_td = tds[-1]
    font = last_td.find("font") # 最后一个td中的font
    if not font or font.get("color") != "green":
        continue
    # 剩下的都是绿色的
    print([td.text.strip() for td in tr.find_all("td")])
