from selenium import webdriver
from time import sleep
from selenium.webdriver.edge.service import Service
"""启动引擎"""
selenium_path ='msedgedriver.exe'
# 通过service方法打开路径
service = Service(selenium_path)
# 再去调用
browser = webdriver.Edge(service=service)
# 访问网址

url = 'https://www.baidu.com'
browser.get(url)

# 元素定位
button = browser.find_element('id', 'su')
print(button)

browser.find_element('name', 'wd')
print(button)

sleep(5)
browser.quit()


