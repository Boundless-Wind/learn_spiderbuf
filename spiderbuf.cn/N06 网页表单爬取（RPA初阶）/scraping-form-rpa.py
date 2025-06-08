import requests
from bs4 import BeautifulSoup

url = r"https://spiderbuf.cn/web-scraping-practice/scraping-form-rpa"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

form_tag = soup.find("form")
for input_tag in form_tag.find_all("input"):
    attr_name = input_tag.get('name')
    input_value = input_tag.get('value')

    match attr_name:
        case 'username':
            print(f'用户名:{input_value}')
        case 'password':
            print(f'密码:{input_value}')
        case 'email':
            print(f'邮箱:{input_value}')
        case 'website':
            print(f'网站:{input_value}')
        case 'date':
            print(f'生日:{input_value}')
        case 'time':
            print(f'时间:{input_value}')
        case 'number':
            print(f'数量:{input_value}')
        case 'range':
            print(f'滑块:{input_value}')
        case 'color':
            print(f'颜色:{input_value}')
        case 'search':
            print(f'搜索:{input_value}')
        case 'gender':
            if input_tag.get('checked') != '':  # 被选中
                print(f'性别:{input_value}')
        case 'interest':
            if input_tag.get('checked') != '':
                print(f'开发语言:{input_value}')

select_tag = form_tag.find("select", {"id": "country"})
for option in select_tag.find_all("option"):
    attr_name = option.get('selected')
    option_value = option.get('value')
    if attr_name != '':
        print(f'人物代表:{option_value}')

ul_tag = form_tag.find("ul", {"class": "items"})
for a_tag in ul_tag.find_all("a"):
    attr_name = a_tag.get('class')
    li_value = a_tag.text
    if 'active' in attr_name:
        print(f'代表人物出处：{li_value}')

# 表单通常由 <form> 标签对包含起来，
# 其中的 name 属性值是必须的且是唯一的，
# 控件的 value 属性存储着值，
#     text
#     password
#     tel
#     email
#     url
#     Date pickers (date, month, week, time, datetime, datetime-local)
#     number
#     range
#     color
#     search
#     textarea
# 某些属性有 checked 属性
#     radio
#     checkbox
# 某些属性是 selected 属性
#     select
