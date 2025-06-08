import requests
import json

import random
import hashlib
import time


def getIrisData(page):
    random_num = int(random.random() * (0xba7af ^ 0xbb8ef) + (0xbe628 ^ 0xbe1f8))   # 生成随机数（等效于JS的Math.floor实现）
    timestamp = int(time.time() * 1000) // (0x54458 ^ 0x547b0)  # 计算毫秒级时间戳参数
    xor_result = page ^ timestamp   # 计算异或结果
    hash_value = hashlib.md5(f"{xor_result}{timestamp}".encode()).hexdigest()   # 生成MD5哈希值
    # 构建返回数据
    return {
        "xorResult": xor_result,
        "random": random_num,
        "timestamp": timestamp,
        "hash": hash_value
    }

sepal_width_num = 0
url = r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c03"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"}

for page in range(1, 6):
    response = requests.post(url,json=getIrisData(page),headers=headers)
    for data in response.json():
        # print(data)
        sepal_width_num += data["sepal_width"]

print(f"{sepal_width_num:.2f}")