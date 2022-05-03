# 适用场景: 数据采集的时候,需要绕过登陆, 然后进入某个页面
# 个人信息页面是utf-8 但还是报错了编码错误, 因为并没有进入到个人信息页面,而是跳转到了登陆页面
# 那么登陆页面不是utf-8 所以报错

import urllib.request

url = 'https://weibo.cn'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
    'cookie': 'x'

}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)