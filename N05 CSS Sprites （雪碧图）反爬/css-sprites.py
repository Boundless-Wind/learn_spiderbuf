import requests
from bs4 import BeautifulSoup

# 这题里，css偏移是固定的，直接手动构造字典
css_dict = {
    "abcdef": "0",
    "ghijkl": "1",
    "mnopqr": "2",
    "uvwxyz": "3",
    "yzabcd": "4",
    "efghij": "5",
    "klmnop": "6",
    "qrstuv": "7",
    "wxyzab": "8",
    "cdefgh": "9",
}

css_mask = "rbmsak"

url = r"https://spiderbuf.cn/web-scraping-practice/css-sprites"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# 雪碧图本质和偏移没什么区别
# 都属于古典密码学的换位而已
# 所以只要找到对应的密钥即可

# 除此之外，雪碧图是偏移一张图片，所以除了人眼处理外，那就上OCR

div_tag = soup.find("div", {"class": "row"}).find_all("div", {"class": "col-xs-6 col-lg-4"})
for div in div_tag:
    p2_tag = div.find_all("p")[1]
    for span in p2_tag.find_all("span"):
        p2_tag.append(css_dict[span["class"][1]])
        span.decompose()
    print(repr(div.text))
