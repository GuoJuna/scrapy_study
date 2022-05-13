import scrapy
import json


class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['fanyi.baidu.com']
    # post 请求 如果没有参数,那么这个请求将没有如何意义
    # 所以start_urls也没有用了
    # parse方法也没有用
    start_urls = ['https://fanyi.baidu.com/sug']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)
