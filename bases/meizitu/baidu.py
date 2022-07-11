import requests
from lxml import etree

URL = 'https://www.mzitu.com/page/'
# URL = 'https://image.baidu.com/search/index'
# URL = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B7%E7%BE%B0&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'


class Graber:
    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            # "Referer": "https://www.mzitu.com/xinggan/"
        }

    def loadData(self):
        for i in range(1, 2):
            print('==========正在抓取%s页==========' % i)
            res = requests.get(URL, headers=self.headers).content
            print(res)
            
            # html = etree.HTML(res.content.decode())
            # self.saveData(html)

    def saveData(self, html):
        print(html.xpath("//ul[@class='imglist']"))
        # print(html.xpath('//ul[@class="imglist"]/li/a/img/@alt'))
        srcs = html.xpath(
            '//ul[@class="imglist"]/li/div[@class=imgbox]/a/img[@class=main_img]')
        alts = html.xpath('//ul[@id="pins"]/li/a/img/@alt')
        for src, alt in zip(srcs, alts):
            fileName = alt+'.jpg'
            res = requests.get(src, headers=self.headers)
            print("正在抓取图片：" + fileName)
            try:
                with open('D://meizitu//'+fileName, "wb") as file:
                    file.write(res.content)
            except:
                print("==========文件保存错误！==========")


graber = Graber()
graber.loadData()
