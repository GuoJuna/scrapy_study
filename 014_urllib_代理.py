import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问
# urllib.request.urlopen(request)

proxies = {
    'http': '47.106.105.236:80'
}

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decord('utf-8')

with open('daiLi.html', 'w', encoding='utf-8') as fp:
    fp.write(content)








