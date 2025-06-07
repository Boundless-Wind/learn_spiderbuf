from selenium import webdriver
from selenium.webdriver.common.by import By

# 浏览器配置优化（增强反反爬能力）
edge_path = r"./../software/msedgedriver.exe"
options = webdriver.EdgeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Edge(options=options, service=webdriver.EdgeService(edge_path))
driver.implicitly_wait(15)  # 智能等待、隐形等待，等待元素存在直接返回，否则直到超时

try:
    driver.get(r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c04")
    captcha = driver.find_element(By.ID, "captcha")
    captcha.click()

    posts = driver.find_element(By.ID, "posts").find_elements(By.CLASS_NAME,"post")
    total = 0
    count = 0

    for post in posts:
        # 定位统计信息容器
        stats = post.find_element(By.CLASS_NAME, 'stats')
        spans = stats.find_elements(By.TAG_NAME, 'span')

        # 提取阅读数（第一个span）
        read_count = int(spans[0].text.split(': ')[1])

        # 提取评论数（第四个span的嵌套数字）
        comments_digits = spans[3].find_elements(By.CLASS_NAME, 'digit')
        comment_count = int(''.join([d.text for d in comments_digits]))

        total += (read_count + comment_count)
        count += 1

    # 计算平均值（保留两位小数）
    if count > 0:
        average = round(total / count, 2)
        print(f"阅读数+评论数平均值: {average}")
    else:
        print("未找到有效数据")

finally:
    driver.quit()
