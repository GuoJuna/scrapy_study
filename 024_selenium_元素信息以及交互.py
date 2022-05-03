from selenium import webdriver
from time import sleep

path = 'msedgedriver.exe'

browser = webdriver.Edge()

url = 'https://www.baidu.com'
browser.get(url)

input = browser.find_element('id', 'su')

# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)

print(input.text)

sleep(5)
browser.quit()

