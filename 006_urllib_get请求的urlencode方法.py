import urllib.parse
import urllib.request


# urlendcode应用场景: 多个参数的时候

url = 'https://www.baidu.com/s?'

data = {
    'wd': '张三',
    'sex': '男',
    'location': '上海'
}

new_data = urllib.parse.urlencode(data)
url = url + new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)