# 请求对象的地址
# 获取网页的源码
# 下载

# 需求 下载前十页的图片
import urllib.request
from lxml import etree

def create_request(page):
    url = 'https://sc.chinaz.com/tupian/meinvxiezhen.html'
    if page != 1:
        url = 'https://sc.chinaz.com/tupian/meinvxiezhen_'+str(page)+'.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//*[@id="container"]//a/img/@alt')
    src_list = tree.xpath('//*[@id="container"]//a/img/@src2')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src

        urllib.request.urlretrieve(url=url, filename='./loveImg/'+name+'.jpg')


if __name__ == '__main__':
    start_page = int(input("请输入起始页码: "))
    end_page = int(input("请输入结束页码: "))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)