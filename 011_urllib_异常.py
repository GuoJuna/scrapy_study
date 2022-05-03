import urllib.request
import urllib.error

url = 'http://www.baidu.ocm'

try:
    response = urllib.request.urlopen(url)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级...')
except urllib.error.URLError:
    print('网络异常!!!')
