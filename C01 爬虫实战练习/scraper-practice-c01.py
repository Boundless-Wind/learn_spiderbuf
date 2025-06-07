import urllib.parse

import requests
from bs4 import BeautifulSoup
import csv

url = r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01"
# url = r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01/mnist"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

# 初始界面
session = requests.Session()
response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

parse_url = urllib.parse.urlparse(url)
base_url = parse_url.scheme + "://" + parse_url.netloc

items = soup.find("ul", {"class": "items"}).find("a")
href = items.get("href")
mnist_url = urllib.parse.urljoin(base_url, href)
print(mnist_url)

# 2级页面，会有cookie存在，所以直接使用session管理会话
mnist_response = session.get(mnist_url, headers=headers)
# print(mnist_response.url)
mnist_soup = BeautifulSoup(mnist_response.text, "lxml")
# print(mnist_soup.prettify())
table = mnist_soup.find("table", {"class": "table"})
sum = num = 0
with open('mnist.csv', 'w', encoding="utf-8-sig", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(table.find("thead").stripped_strings)
    for tr in table.find("tbody").find_all("tr"):
        tds = tr.find_all("td")
        writer.writerow([td.text for td in tds])
        sum += int(tds[1].text)
        num += 1

print(f"{sum/num:.2f}")