import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

# 将周杰伦三个字编程unicode编码
# 我们需要依赖于urllib.parse
name = urllib.parse.quote("周杰伦")
url = url + name

# 请求对象的定制
request = urllib.request.Request(url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)