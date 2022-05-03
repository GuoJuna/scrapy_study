import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 将数据下载到本地 open方法默认使用的gbk的编码, 如果要保存汉子,需要open方法中指定编码utf-8
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)

# with写法
with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
