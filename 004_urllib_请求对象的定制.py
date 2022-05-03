import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?wd=周杰伦

# http/https   www.baidu.com   80/443    s      wd = 周杰伦   #
#   协议             主机         端口     路径       参数      锚点

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

# 因为urlopen方法中不能存储字典, 所以headers不能传递进去
# 请求对象的定制
request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)