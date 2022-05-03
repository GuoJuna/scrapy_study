proxies_pool = [
    {'http': '118.24.219.151:1212'},
    {'http': '118.24.219.151:2222'}
]

import random
import urllib.request

proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

print(content)