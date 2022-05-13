1. 创建项目 scrapy startproject 项目的名字
2. 跳转到spriders文件夹的目录下
    cd 项目名字\项目名字\spiders
3. 创建爬虫文件
    scrapy genspider -t crawl 爬虫文件的名字 爬虫的域名
4. 安装pymsql
   pip install pymysql -i https://pypi.douban.com/simple
   pip3 install pymysql -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com