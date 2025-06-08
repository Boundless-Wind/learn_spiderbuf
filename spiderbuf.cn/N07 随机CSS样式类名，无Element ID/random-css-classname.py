import requests

url = r"https://spiderbuf.cn/web-scraping-practice/random-css-classname"

# 这道题有问题，原本每次刷新的CSS标签应该不一样，但实际是一样的

# 这道题的解法有两种
# 1. 解析style标签中的CSS标签
# 2. 使用相对定位：main标签下的第2个div下的div