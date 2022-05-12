# 通过登陆, 然后进入到主页面

# __VIEWSTATE: bSKboK9zhuja4r1j6ijGdmjZK4Ooleh0BLdwRjtHCInmema3x30WLYjjtf39/pCAoE1fYflQF5fBczNvlJWAreerC5Uze76ZuQ2G+yhP/LqNYQBF6zP83sEwwDQ=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 13384720296
# pwd: gfgsdgsdfgdfgfd
# code: r49h
# denglu: 登录

# 难点 __VIEWSTATE __VIEWSTATEGENERATOR code的值获取

import requests
from bs4 import BeautifulSoup

# 登陆页面的URL地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

# 获取页面源码
response = requests.get(url=url, headers=headers)
content = response.text

# 解析页面源码
soup = BeautifulSoup(content, 'lxml')

# 获取 __VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
# 获取 __VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code

# 获取了验证码的图片之后, 下载到本地 然后观察图片 观察之后, 然后在控制台输入这个验证码, 就可以将这个值赋值个code
session = requests.session()
response_code = session.get(code_url)
# 注意此时要使用二进制数据, 因为我们要使用的图片的下载
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

code_name = input('请输入你的验证码:')
# 点击登陆
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '_VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13384720296',
    'pwd': '123456',
    'code': code_name,
    'denglu': '登录',
}

content_post = session.post(url=url_post, headers=headers, data=data_post)
text = content_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(text)
