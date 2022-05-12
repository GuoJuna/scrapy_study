import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
# Response类型
print(type(response))

# 设置响应的编码的格式
response.encoding = 'utf-8'

# 以字符库形式来返回的网页源码
print(response.text)

# 返回一个url地址
print(response.url)

# 返回的是二进制的数据
print(response.content)

# 响应码
print(response.status_code)

# 响应头信息
print(response.headers)