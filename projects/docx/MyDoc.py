from docx import Document
import os
from win32com import client as wc
from time import sleep


#path = 'D:/200丨work/220丨doc/项目审计/2020/月度验收报告'
#docx = 'D:/200丨work/220丨doc/项目审计/2020/docx'
#replace = 'D:/200丨work/220丨doc/项目审计/2020/replace/'

path = 'E:\900丨Other\周报'
docx = 'E:\900丨Other\周报_new'

# old_path = 'E:\900丨Other\周报'
# new_path = 'E:\900丨Other\周报_new'
replace = 'E:/新建文件夹/old/研发周报/replace/'


class MyDoc:
    """批量处理docx文件"""

    def __init__(self, old_info, new_info) -> None:
        """定义文件路径等"""

        self.old_info = old_info
        self.new_info = new_info
        self.path = str(path)

    def save_doc_to_docx(self, files):
        """doc转换docx"""

        for file_name in files:

            word = wc.Dispatch('Word.Application')

            docx_name = file_name.split('.')[0]+'.docx'
            path = u'%s/' % self.path + file_name
            docx_path = u'%s/' % docx + docx_name
            if os.path.exists(docx_path):
                print('exists')
                continue

            print(path)
            print(docx_path)

            doc = word.Documents.Open(path)
            # 目标路径下的文件
            doc.SaveAs(docx_path, 12)
            doc.Close()
            word.Quit()
            sleep(2)

    def rename(self, files):
        """批量修改文件名"""

        for file_name in files:
            oldname = '%s/' % self.path + file_name
            # newname = '%s/' % self.path + \
            #     file_name.replace(' ', '')
            newname = '%s/' % self.path + \
                file_name.replace(self.old_info, self.new_info)
            os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名

    def get_files(self):
        """从文件夹路径获取文件列表"""

        files = []
        # 从文件夹路径获取文件列表,并剔除非docx格式的文件
        for file in os.listdir(self.path):
            if file.endswith('.docx'):
                files.append(file)
            else:
                print(file)
        print(files)
        # self.rename(files)
        # self.doc2docx(files)
        # self.read(files)

    def read(self, files):
        """读取所有文件"""
        for file in files:

            print(self.path+'/'+file)
            print(replace + file.split("/")[-1])
            doc = Document(self.path+'/'+file)
            self.update(doc)
            doc.save(self.path+'/'+file)
            print("{}替换完成".format(file))

    def update(self, doc):
        """替换文件内容"""

        # 读取所有段落里面的内容并替换
        for p in doc.paragraphs:
            for run in p.runs:
                run.text = run.text.replace(self.old_info, self.new_info)

        # 读取所有表格里面的内容并替换
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    cell.text = cell.text.replace(
                        self.old_info, self.new_info)  # 替换信息


mydoc = MyDoc('基于深度学习的人机交互智能服务系统', '基于深度学习的人机交互智能服务系统')
mydoc.get_files()
