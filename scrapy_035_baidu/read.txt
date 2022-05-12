1. 创建爬虫项目 scrapy startproject 项目的名字
                                    注意: 项目的名字不允许石笋数字开头, 也不能包含中文
2. 创建爬虫文件
        要在spiders文件夹中去创建爬虫文件
        cd 项目的名字\项目的名字\spiders
        cd scrapy_baidu_033\scrapy_baidu_033\spiders

        创建爬虫文件
        scrapy genspider 爬虫文件的名字
        eg: scrapy genspider baidu www.baidu.com

3. 运行爬虫代码
        scrapy crawl 爬虫的名字
        eg: scrapy crawl baidu