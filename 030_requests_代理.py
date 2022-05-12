import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

data = {
    'wd': 'ip'
}

proxy = {
    'http': '121.230.210.31:3256'
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)

content = response.text

with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
