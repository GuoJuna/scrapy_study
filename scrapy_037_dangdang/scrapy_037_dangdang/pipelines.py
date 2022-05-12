# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道, 那么必须在settings中开启管道
class Scrapy037DangdangPipeline:
    # 在爬虫文件开始之前执行方法
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 以下这种模式不推荐, 因为没传递过来一个对象, 就打开一次文件 对文件的操作过于频繁
        # (1) writer方法必须要写一个字符串 而不跟你使用其他对象
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))

        # 不会重复打开文件
        self.fp.write(str(item))
        return item

    # 在爬虫文件执行完之后 执行的方法
    def close_spider(self, spider):
        self.fp.close()


import urllib.request


# 多条管道开启
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = 'https:'+item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
