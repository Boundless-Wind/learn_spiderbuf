import json
from base64 import b64encode, b64decode
from hashlib import sha256
from hmac import new
from time import time, perf_counter

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# 这道题除了参数有混淆以外，返回值也做了加密

url = r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c08"
headers = {
    "Referer": "https://spiderbuf.cn/web-scraping-practice/scraper-practice-c08",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
}


def get_payload():
    timestamp = int(time())  # 计算秒级时间戳
    # 模拟performance.now()（获取高精度时间差，单位：毫秒），注意：Python中无法直接获取页面加载时间，这里用程序运行时间近似替代
    performance_now = int(perf_counter() / 10)  # 转换为秒
    salt = b64encode(f"{performance_now}".encode()).decode()
    hash = new(url.encode(), f"{salt}{timestamp}".encode(), sha256).digest()  # 对时间戳和盐签名
    signature = b64encode(hash).decode()

    # 构建返回数据
    return {
        "t": timestamp,
        "s": salt,
        "sig": signature,  # requests会自动对其 url编码
    }


def get_result(data, signature):
    # 提取密钥（前16个UTF8字符）
    key = signature[:16].encode('utf-8')

    # 解码Base64数据
    decoded_data = b64decode(data['d'])

    # 拆分IV（前16字节）和密文（剩余部分）
    iv = decoded_data[:16]
    ciphertext = decoded_data[16:]

    # 创建AES解密器（CBC模式，PKCS7填充）
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 解密并去除填充
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)

    # 解析JSON结果
    return json.loads(plaintext.decode('utf-8'))


api_url = r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c08/api"
params = get_payload()
response = requests.get(api_url, params=params, headers=headers)
data = response.json()
print(params)
print(data)

# params = {
#     't': 1749392151,
#     's': 'MzUzMQ==',
#     'sig': 'rfzcw9jXa6AQ5jckjnW+s6OwPauGyI9rCQuV+mzOgkE='
# }
#
# data = {
#     'd': 'xG2dUtD6EckOt6AavM9GPfYJSHXKfo8+Cv/2qhvwJkMwwlg4zkq9r6Q5gfZ8aMAs+825ckE01+6nOX9VCe0os0KiYwQqrJ8SW7R6m0dFOBNK291MV8fBTTVkYQwdAV5dsvUIM9tAiXPxyM4VFwlS5mhOalGwNT0FGZC5P1hamrzXKHgsHTNSOez2PlrmLKCALL1+gJmSr7rHpO4iXlQ0WhPRbVKmT9krLfSfYBRliY38WF5Pn0I/z0ksqpI56JqNJVbZexjjWlaq/ilyVBLP5gWvAf8mk1Qh7QImZN1U4gfqlrG1uwpQfjc6a/zu11jBDZKJqhNJS40mJ7hWiRVvoaSkZmjPFm9fb7PWCYqM0vcXeUZJqMuRbGiMPKxkvFDadYa6GHzM6WmIKrtRMyk0JCMdPUL+iqlfX7KVAoHrQzwJkktqpVLymhZwTH7WZAGe2bBKafgycm7onG7+z7HpvVJRghSDbEss7W6zM58FFAbQlIjik28iyGAsonRR6gaHOzlPMOBGJxSrRaXrSwDIxsttb7B2uHqYw2IOc4Pclfj6aj6V2bLng3nCW4MtPytZqEi11/HeLDadNb0GKTnnT1jYxJ5p37ZMbr06lT6AJFF/2K29XwFRMaDICup6Gxm/jxd8JJBjBxw8pe/pe6FYHuptUe0po4T30wfEm32P83BaCJnsoth9BuPm/LBS76q4kFYslsSsXZNpf3MED1l7YlbpxoSVJJWc2yV6M2nHYDYaZOT323KxbIOS+QDm6syLd1keL3oJQ2dzHbdTyqjR49KyHmR5NrbJhlVj4+EKEiKuWbhvGa3I9LygxiKLZ/lPa0omEqOz2IJI62ZZgCxZsDXT4Pb2+s0ZIpM94xQ0xkHptCEOIuC/ulOZ/5CPYABCBxcbKPt4ce39B/6N0gdEDiu/gSVa2JpixT5BGW09RSr178NZkBiz/qsrp0bfbaEumm2yxu46TEa00QdhTgaOTOBIrHDqPytsY8ZAjkerDyIsfg1oty5OhvfbnFI+nhsjv0u2meWe2HvUd754CzajNuOYDJP2FEBeNQ0r9ucWjan34dqUQ+8s7m6UlHX32YY2xpiARZG+6LcRuypI+UCUPP23kjcxEu5gYWdycPazS6gw0CjgusX9QokZQYqTbe3xv3ofu7wg5piMSG/p7QF2pqxkjo5v9eakkgB2wBLTqfy7D+3qrerNz+KIJ0cCRyQQG0/EqJkJyIcEf04qzF05Zetqwp2B2Q3xQjTEp0CG18EdqdBRYAG6mDrjKBqnP9F9kT1C3PzLZVqDgdt9R+p1X0n0WOcbEqfA3Qhp1Dshg99ygAjtTOoBelRnLq43YpeIiw7C61818W8n1omNBT2iT6ppjdvygS4WEs0BotE8vs8XsW5O/UzinsBirOr/7RoUHfFGnRhoKMD863OLVZAVT8I6vBg59hSX2uIJFPZvRwegXBfJNKQufj23EBDFNNhR6K97ZLz1+vMjGg9pLiXl9eeUDCIRIhaIMYiavGCgfelVQ6wKyilmfKJtCB1DlkpvqABdIJxWEcRxe/ftvj1KLgJwJKk4P8xK7wKTfQ+6yO/QEAdDNRKawysIpLIPr+cex/X4CyOSGNgajnCOdTvaA98vlAtwtyVzkQYl5D/WA32CTAaoevY1lOeT/Nb3vBaTKRLKF8mGaJIFz48kdCGI5yH7yk30zqucE7O3OWl78WTA0MddBe6FsS+rQhVPM3NqRPG4HSeRU81jZPOmfNbpL3IWKn1Lp0iGq8+m33IPVtsQ9BXNmGvK1CsE1a3oYVyTvjxqQl29jIwsCPRyRzR1XQr2Wj6gMWE2FXD7eeDFykMwz2tkDYd9RJdLmRzMZ83GUmeA4605za8C2HPrCuQ/Dg==',
#     'i': 'XAQ2ZpDdaFWJkgPk',
#     'k': 'JQiXJpeBoh8K8Vmb'
# }

result = get_result(data, params["sig"])
print(result)
# [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'price': 245.67, 'market_cap': '3.72T', 'volume': '45.2M', 'change': 1.23, 'source': 'Yahoo! Finance'}, {'symbol': 'MSFT', 'name': 'Microsoft Corporation', 'price': 420.15, 'market_cap': '3.11T', 'volume': '22.8M', 'change': -0.45, 'source': 'Yahoo! Finance'}, {'symbol': 'GOOGL', 'name': 'Alphabet Inc.', 'price': 175.89, 'market_cap': '2.15T', 'volume': '30.1M', 'change': 0.87, 'source': 'Yahoo! Finance'}, {'symbol': 'AMZN', 'name': 'Amazon.com, Inc.', 'price': 208.34, 'market_cap': '2.18T', 'volume': '41.5M', 'change': 2.11, 'source': 'Yahoo! Finance'}, {'symbol': 'NVDA', 'name': 'NVIDIA Corporation', 'price': 135.22, 'market_cap': '3.35T', 'volume': '210.3M', 'change': 3.45, 'source': 'Yahoo! Finance'}, {'symbol': 'TSLA', 'name': 'Tesla, Inc.', 'price': 420.76, 'market_cap': '1.34T', 'volume': '98.7M', 'change': -1.89, 'source': 'Yahoo! Finance'}, {'symbol': 'META', 'name': 'Meta Platforms, Inc.', 'price': 595.12, 'market_cap': '1.50T', 'volume': '15.6M', 'change': 0.56, 'source': 'Yahoo! Finance'}, {'symbol': 'JPM', 'name': 'JPMorgan Chase & Co.', 'price': 225.45, 'market_cap': '645.8B', 'volume': '8.9M', 'change': 0.33, 'source': 'Yahoo! Finance'}, {'symbol': 'V', 'name': 'Visa Inc.', 'price': 290.67, 'market_cap': '560.2B', 'volume': '6.7M', 'change': -0.12, 'source': 'Yahoo! Finance'}, {'symbol': 'MA', 'name': 'Mastercard Incorporated', 'price': 510.34, 'market_cap': '475.1B', 'volume': '2.4M', 'change': 0.78, 'source': 'Yahoo! Finance'}]


price_total = 0
price_num = 0

for item in result:
    price_total += float(item['price'])
    price_num += 1

print(round(price_total / price_num, 2))
