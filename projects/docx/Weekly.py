from docx import Document
import os
from win32com import client as wc
from time import sleep

from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.shared import Cm, Pt

#path = 'D:/200丨work/220丨doc/项目审计/2020/月度验收报告'
#docx = 'D:/200丨work/220丨doc/项目审计/2020/docx'
#replace = 'D:/200丨work/220丨doc/项目审计/2020/replace/'

path = 'E:\900丨Other\周报'
new_path = 'E:\900丨Other\周报\\'
# new_path = 'E:\900丨Other\周报_new\\'

# old_path = 'E:\900丨Other\周报'
# new_path = 'E:\900丨Other\周报_new'
# replace = 'E:/新建文件夹/old/研发周报/replace/'


class Weekly:
    """周报处理"""

    def __init__(self,) -> None:
        """定义文件路径等"""

        self.path = str(path)
        self.new_path = str(new_path)

    def get_files(self):
        """从文件夹路径获取文件列表"""

        index = 0
        # 从文件夹路径获取文件列表,并剔除~$开头的文件
        for dir in os.listdir(self.path):
            if dir.startswith('~$'):
                print(dir)
            else:
                for file in os.listdir(self.path+'\\'+dir):
                    index += 1
                    if file.endswith('.doc') and (not file.startswith('~$')):
                        index += 1
                        file_name = self.path+'\\'+dir+'\\'+file
                        # os.remove(file_name)
                        # self.read(file_name)
                        # self.save_doc_to_docx(file_name)
                    else:
                        print(file)

        print(index)

    def save_doc_to_docx(self, file_name):
        """doc转换docx"""

        word = wc.Dispatch('Word.Application')

        docx_name = file_name.split('.')[0]+'.docx'

        if os.path.exists(docx_name):
            print('exists')
        else:
            try:
                doc = word.Documents.Open(file_name)
                # 目标路径下的文件
                doc.SaveAs(docx_name, 12)
                doc.Close()
                word.Quit()
                sleep(2)
            except IOError:
                print(docx_name)
            else:
                pass

    def read(self, file_name):
        """读取所有文件"""
        doc = Document(file_name)
        self.update(doc)
        doc.save(file_name)
        print("{}修改完成".format(file_name))

    def update(self, doc):
        """替换文件内容"""

        table = doc.tables[0]

        row = table.rows[1]
        cell = row.cells[3]

        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        cell.text = '唐永辉'

        run = cell.paragraphs[0].runs[0]

        run.font.name = '微软雅黑'
        run.font.size = Pt(10.5)


mydoc = Weekly()
mydoc.get_files()
