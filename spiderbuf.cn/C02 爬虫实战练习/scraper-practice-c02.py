import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 浏览器配置优化（增强反反爬能力）
edge_path = r"../../software/msedgedriver.exe"
options = webdriver.EdgeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Edge(options=options, service=webdriver.EdgeService(edge_path))
driver.implicitly_wait(15)  # 智能等待、隐形等待，等待元素存在直接返回，否则直到超时

try:
    driver.get(r"https://spiderbuf.cn/web-scraping-practice/scraper-practice-c02")

    # 方案二：模拟人类拖拽（备用方案）
    slider = driver.find_element(By.ID, 'slider')  # w:50
    container = driver.find_element(By.CLASS_NAME, 'container')  # w:300

    container_width = container.rect['width']  # 获取容器宽度
    slider_width = slider.rect['width']  # 获取滑块宽度
    print("容器宽度:", container_width)
    print("滑块宽度:", slider_width)

    actions = ActionChains(driver)
    actions.click_and_hold(slider).perform()  # 300-50=250

    # 模拟人类拖拽轨迹（带随机抖动）
    num = 5
    per = (container_width - slider_width) / num
    for x in range(0, num):
        actions.move_by_offset(
            xoffset=per,
            yoffset=random.randint(-2, 2)
        ).perform()
        # time.sleep(random.random())  # 随机延迟

        # 实时检查是否通过验证    # 正常是白色，通过是绿色
        if container.value_of_css_property('background-color') == 'rgba(0, 193, 110, 0.98)':
            break

    actions.release().perform()

    # 验证是否成功
    if container.value_of_css_property('background-color') == 'rgba(0, 193, 110, 0.98)':
        print("验证通过！")
        # 提取表格数据
        rows = driver.find_elements(By.CSS_SELECTOR, '#flightTable tbody tr')
        prices = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) >= 3:
                try:
                    # 提取价格并转换为数字（处理可能的中文单位）
                    price_str = cells[2].text.replace('元', '').strip()
                    prices.append(float(price_str))
                except ValueError:
                    pass  # 跳过无效价格

        average_price = round(sum(prices) / len(prices), 2) if prices else 0
        print(f"机票价格平均值：{average_price:.2f}元")
    else:
        print("验证失败")
finally:
    driver.quit()
