import requests
import bs4
import os

URL = 'https://www.mzitu.com/page/'
save_url = 'D://900丨other//mzitu/'


class Grappler():
    """抓取网路文件的类"""

    def __init__(self, url, save_url, page_number=1) -> None:
        """定义抓取网络文件的地址、保存地址、headers"""

        self.url = url
        self.save_url = save_url
        self.page_number = page_number
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.mzitu.com/xinggan/"
        }

    def start(self):
        """开始抓取网络文件"""

        for i in range(1, self.page_number+1):
            print('正在抓取第%d页' % i)
            response = requests.get(self.url+str(i), headers=self.headers)
            self.save(response)

    def save(self, response):
        """保存文件到本地"""

        images = bs4.BeautifulSoup(response.text).select('li>a>img')
        for image in images:
            src = image.get('data-original')
            file_name = image.get('alt')+'.jpg'

            """获取图片"""
            image_res = requests.get(src, headers=self.headers)

            # 判断保存文件的路径是否存在，不存在则创建，存在则继续保存文件
            if not os.path.exists(self.save_url):
                os.mkdir(self.save_url)
            else:
                try:
                    # 打开并保存文件
                    with open(self.save_url+file_name, 'wb') as file:
                        file.write(image_res.content)
                except:
                    print('保存文件有误')


grappler = Grappler(URL, save_url, 254)
grappler.start()
