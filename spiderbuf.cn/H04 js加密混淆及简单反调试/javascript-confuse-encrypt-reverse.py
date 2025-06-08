import json

import requests

# url = r"https://spiderbuf.cn/web-scraping-practice/javascript-confuse-encrypt-reverse"
url = r"https://spiderbuf.cn/static/js/h04/udSL29.js"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

response = requests.get(url, headers=headers)
raw_data = response.text.split(";", maxsplit=1)[0].split("=")[-1]
# data = json.loads(raw_data)
data = eval(raw_data)
print(type(data),data)

# js过调试和混淆
# 被调试的原理是自动或手动的添加定时函数去debugger
# 过调试有很多方法，例如：替换函数，或是手动打断点

# 而混淆则是将js原本的代码变成分析起来很麻烦的代码，可以去一些网站反混淆
