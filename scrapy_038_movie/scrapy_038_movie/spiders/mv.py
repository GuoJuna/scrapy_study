import scrapy

from scrapy_038_movie.items import Scrapy038MovieItem


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 要第一页的名字和第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            url = a.xpath('./@href').extract_first()
            name = a.xpath('./text()').extract_first()

            # 第二页地址是
            url = 'https://www.ygdy8.net' + url
            # 对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # 注意 如果拿不到数据 一定要检查你的xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']

        movie = Scrapy038MovieItem(src=src, name=name)
        yield movie
