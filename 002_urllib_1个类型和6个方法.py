import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse
# print(type(response))

# 安装一个字节一个字节的去读
content = response.read()
print(content)
print("------------分割线------------")

# 读取一行
content = response.readline()
print(content)
print("------------分割线------------")

# 一行一行读 直到读完
content = response.readlines()
print(content)
print("------------分割线------------")

# 返回状态码
print(response.getcode())
print("------------分割线------------")

# 返回url地址
print(response.geturl())
print("------------分割线------------")

# 获取状态信息
print(response.getheaders())

# 一个类型hTTPResponse
# 六个方法 read readline readlines getCode getUrl getheaders
