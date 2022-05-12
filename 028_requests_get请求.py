# urllib
# 1. 一个类型和六个方法
# 2. get请求
# 3. post请求
# 4. ajax的get请求
# 5. ajax的post请求
# 6. cookie登陆
# 7. 代理

# requests
# 1. 一个类型和六个属性
# 2. get请求
# 3. post请求
# 4. 代理
# 5. cookie 验证码

import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

data = {
    'wd': '北京'
}

response = requests.get(url=url, params=data, headers=headers)
content = response.text

print(content)

# (1)参数使用params传递
# (2)参数无需urlencode编码
# (3)不需要请求对象的定制
# (4)请求资源路径中的?可以加也可以不加