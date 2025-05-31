import base64
import hashlib
import time

import requests

# url = r"https://spiderbuf.cn/web-scraping-practice/javascript-reverse-timestamp"
url = r"https://spiderbuf.cn/web-scraping-practice/javascript-reverse-timestamp/api/{s}"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}

timeStamp = str(int(time.time()))
_md5 = hashlib.md5(timeStamp.encode()).hexdigest().lower()
s = timeStamp + "," + _md5
temp_url = url.format(s=base64.b64encode(s.encode()).decode())
print(temp_url)
response = requests.get(temp_url, headers=headers)
print(response.json())

# s = timeStamp+","+md5(timeStamp)
