# (1) 获取网页的源码
# (2) 解析 解析的服务器响应的文件 etree.HTML
# (3) 打印

import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 解析网页源码 来获取我们想要的数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpath的返回值是一个列表类型的数据
result = tree.xpath('//*[@id="su"]/@value')[0]

print(result)
