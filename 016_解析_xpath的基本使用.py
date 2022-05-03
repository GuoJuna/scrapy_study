from lxml import etree

# xpath解析
# 1. 本地文件  etree.parse
# 2. 服务器响应数据 response.read().decode('utf-8')  etree.HTML()

# xpath解析本地文件
tree = etree.parse('016_解析_xpath的基本使用.html')

# tree.xpath路径

# 查找ul下的li
li_list = tree.xpath('//ul/li')

print(li_list)
print(len(li_list))

# 查找所有有id的属性的li标签 text获取标签的内容
li_list = tree.xpath('//ul/li[@id]/text()')

print(li_list)
print(len(li_list))

# 找到id为bj的li标签 注意引号的问题
li_list = tree.xpath('//ul/li[@id="bj"]/text()')
print(li_list)
print(len(li_list))

# 查找到id为bj的li标签的class的属性值
li = tree.xpath('//ul/li[@id="bj"]/@class')
print(li)

# 查询id中包含b的标签
li_list = tree.xpath('//ul/li[contains(@id,"b")]')
print(li_list)

# 查询id的值以b开头的标签
li_list = tree.xpath('//ul/li[starts-with(@id,"b")]')
print(li_list)

# 查询id为bj和class为c1的
li_list = tree.xpath('//ul/li[@id="bj" and @class="c1"]/text()')
print(li_list)

li_list = tree.xpath('//ul/li[@id="bj"]/text() | //ul/li[@id="sh"]/text()')
print(li_list)