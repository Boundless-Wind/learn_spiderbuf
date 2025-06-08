import re

import requests
from bs4 import BeautifulSoup

# 这题里，css偏移是固定的，直接手动构造字典
css_dict = {
    "abcdef": {"before": "7", "after": "5"},
    "ghijkl": {"before": "8", "after": "9"},
    "mnopqr": {"before": "9", "after": "1"},
    "uvwxyz": {"before": "1", "after": "4"},
    "yzabcd": {"before": "2", "after": "6"},
    "efghij": {"before": "3", "after": "2"},
    "klmnop": {"before": "5", "after": "7"},
    "qrstuv": {"before": "4", "after": "3"},
    "wxyzab": {"before": "6", "after": "0"},
    "cdefgh": {"before": "0", "after": "8"},
    "hijklm": {"after": "6"},
    "opqrst": {"after": "0"},
    "uvwxab": {"after": "3"},
    "cdijkl": {"after": "8"},
    "pqrmno": {"after": "1"},
    "stuvwx": {"after": "4"},
    "pkenmc": {"after": "7"},
    "tcwdsk": {"after": "9"},
    "mkrtyu": {"after": "5"},
    "umdrtk": {"after": "2"},
}

css_mask = "rbmsak"

url = r"https://spiderbuf.cn/web-scraping-practice/css-pseudo-elements"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# 这道题的数据获取确实没什么好的规律
# 所以换个方法，直接修改源html
# 添加正确数据，删除误导数据

div_container = soup.find("div", {"class": "container", "style": False})

# 修改源文档
span_need_decompose = div_container.find_all("span", {"class": css_mask})
for span_mask in span_need_decompose:
    span_previous = span_mask.find_previous_sibling("span")
    temp = {}
    for key in span_previous['class']:
        temp.update(css_dict[key])
    text = temp["before"] + "." + temp["after"]
    span_previous.decompose()  # 销毁自己
    # 注意：text本质是get_text，没有setter方法
    # 而string既有getter也有setter
    span_mask.string = text

# 获取文本
rn = re.compile(r'\r\n')
n = re.compile(r'\n+')


def process_text(text):
    text = re.sub(r'\r\n', '', text)  # 1. 删除所有\r\n（Windows换行符）
    text = re.sub(r'\n+', '\n', text)  # 2. 合并连续换行符为单个\n
    text = re.sub(r' +', ' ', text)  # 3. 合并连续空格为单个空格
    return text


rows = div_container.find_all("div", {"class": "col-xs-12 col-lg-12"})
for row in rows:
    print(process_text(row.text.strip()))
    print()

# css偏移解决
# 原理是css的元素的before和after属性中插入文字
# 只要获得before和after对应的文字字典即可

# # 判断是否为特殊节点
# def has_class_and_in_dict(tag: Tag):
#     if not tag.has_attr('class'):
#         return "not_class"
#     elif tag['class'][0] == css_mask:
#         return "is_mark"
#     elif all([t in css_dict for t in tag['class']]):   # 确保所有标签都在偏移字典中
#         return "is_special"
#
# div_container = soup.find("div", {"class": "container", "style": False})
# rows = div_container.find_all("div", {"class": "col-xs-12 col-lg-12"})
# for row in rows[:5]:
#     for tag in row.find_all():
#         if tag.find():  # 确保到叶子节点
#             continue
#         match has_class_and_in_dict(tag):
#             case "not_class":   # 不是特殊节点就要使用普通的解析文本
#                 if text := tag.text.strip():
#                     print(text)
#             case "is_special":  # 是特殊节点就要调用函数解析文本
#                 temp = {}
#                 for key in tag['class']:
#                     temp.update(css_dict[key])
#                 text = temp["before"] + "." + temp["after"]
#                 print(text)
#             case _:
#                 continue
