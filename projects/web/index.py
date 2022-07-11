


class Grappler():
    """抓取网路文件的类"""

    def __init__(self, url, save_url) -> None:
        """定义抓取网络文件的地址、保存地址、headers"""

        self.url = url
        self.save_url = save_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.mzitu.com/xinggan/"
        }

    def start(self):
        """开始抓取网络文件"""
        response = requests.get(self.url, headers=self.headers)
        self.save(response)

    def save(self, response):
        """保存文件到本地"""

        images = bs4.BeautifulSoup(response.text).select('li>a>img')
        for image in images:
            src = image.get('data-original')
            file_name = image.get('alt')+'.jpg'
            print(src)
            print(file_name)

            """获取图片"""
            image_res = requests.get(src, headers=self.headers)

            if not os.path.exists(self.save_url):
                print('exits')
                os.makedirs(self.save_url)
            else:
                try:
                    with open(self.save_url, file_name, 'wb') as file:
                        file.write(image_res.content)

                except:
                    print('保存文件有误')

#     if not os.path.exists(save_url):
#         os.makedirs(file_name)
#     else:
#         try:
#             with open(save_url+file_name, 'wb') as f:
#                 f.write(response.content)
#         except:
#             print("==========文件名有误！==========")

