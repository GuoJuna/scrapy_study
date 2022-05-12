import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['hz.58.com']
    start_urls = ['http://hz.58.com/']

    def parse(self, response):
        content = response.text
        print('===============================')
        print(content)
