from selenium import webdriver

url = r"https://spiderbuf.cn/web-scraping-practice/selenium-fingerprint-anti-scraper"

edge_path = r"./../software/msedgedriver.exe"
service = webdriver.EdgeService(edge_path)

options = webdriver.EdgeOptions()
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'}) # 设置能力
options.add_argument('--disable-blink-features=AutomationControlled')   # 改变navigator.webdriver 属性值

driver = webdriver.Edge(options=options, service=service)

driver.get(url)
print(driver.page_source)

driver.quit()
