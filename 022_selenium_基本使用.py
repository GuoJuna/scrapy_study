# (1)导入selenium
from selenium import webdriver

# (2)创建浏览器操作对象

browser = webdriver.Edge('msedgedriver.exe')

# 访问网站
url = 'https://www.baidu.com'

browser.get(url)
# 获取网页源码
content = browser.page_source
print(content)