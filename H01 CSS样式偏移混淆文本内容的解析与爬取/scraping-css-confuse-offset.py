import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/scraping-css-confuse-offset"

headers = {
    "Referer": "https://spiderbuf.cn/web-scraping-practices/3?order=learn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
divs = soup.find("div", {"class": "row"}).find_all("div", {"class": "col-xs-6 col-lg-4"})


for div in divs:
    temp = []
    for ele in div.find_all(recursive=False):   # 只搜索一层
        if ele.find("i"):
            tags_i = [i.text.strip() for i in ele.find_all()]
            tags_i[0],tags_i[1] = tags_i[1],tags_i[0]   # 调换个位置
            if ele.name == "p":
                # text是获得所有文本；stripped_strings是获得所有文本的生成器
                for title in ele.stripped_strings:
                    tags_i.insert(0, title.strip()) # 只获得第一个值
                    break
            temp.append("".join(tags_i))
            continue
        temp.append(ele.text.strip())
    print(",".join(temp))