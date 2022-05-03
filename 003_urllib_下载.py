import urllib.request

url = 'http://www.baidu.com'
# url代表的是下载路径 filename文件的名字
# 在python中 可以是变量的名字,也可以直接写值
urllib.request.urlretrieve(url, "baidu.html")

# 下载图片
url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.2008php.com%2F09_Website_appreciate%2F10-07-11%2F1278861720_g.jpg&refer=http%3A%2F%2Fwww.2008php.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1653618657&t=e6ad52310fbd65d658026c44d613edba'
urllib.request.urlretrieve(url_img, '123.jpg')

# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-ndr15wddzvxhapx4/sc/cae_h264_delogo/1650934484278250911/mda-ndr15wddzvxhapx4.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1651028585-0-0-86099cee4b5dd42671f457e2f1e05dbb&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=1985049104&vid=14226474851135614437&abtest=100815_1-101454_1-101830_2-17451_1-3000222_4&klogid=1985049104'
urllib.request.urlretrieve(url_video, 'video.MP4')