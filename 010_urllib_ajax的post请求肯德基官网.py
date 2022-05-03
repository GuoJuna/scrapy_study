import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '杭州',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }

    new_data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
    }
    return urllib.request.Request(base_url, new_data, headers=headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def down_load(page, content):
    with open('kfc_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码:'))
    end_page = int(input('请输入结束的页码:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)