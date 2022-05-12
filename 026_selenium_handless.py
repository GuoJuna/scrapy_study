from selenium import webdriver
from selenium.webdriver.edge.options import Options


# 封装的handless
def share_browser():
    edge_options = Options()
    edge_options.add_argument('--headless')
    edge_options.add_argument('--disable-gpu')

    # path是浏览器路径
    path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    edge_options.binary_location = path

    return webdriver.Edge(options=edge_options)


browser = share_browser()
url = 'https://www.baidu.com'
browser.get(url)

browser.save_screenshot('baidu.png')
