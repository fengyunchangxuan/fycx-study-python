import datetime
from docx import Document
import os
from win32com import client as wc
import time
from datetime import datetime
from datetime import timedelta

# old_path = 'D:/200丨work/220丨doc/项目审计/2020/研发周报_old'
# new_path = 'D:/200丨work/220丨doc/项目审计/2020/研发周报_new'
# template = 'D:/200丨work/220丨doc/项目审计/2020/项目研发周报.docx'

old_path = 'E:\900丨Other\周报'
new_path = 'E:\900丨Other\周报_new'

template = 'C:/Users/wxy/Desktop/项目审计/200丨工作/项目研发周报.docx'
project_name = '大数据技术在多媒体信息系统中的研发'


class Mydocx:
    """批量处理docx文件"""

    def __init__(self) -> None:
        """定义文件路径等"""

        self.old_path = str(old_path)
        self.new_path = str(new_path)
        self.template = str(template)

    def next_week(self, date_str, days_count=7):
        date_list = time.strptime(date_str, "%Y年%m月%d日")
        y, m, d = date_list[:3]
        delta = timedelta(days=days_count)
        date_result = datetime(y, m, d) + delta
        date_result = date_result.strftime("%Y年%m月%d日")
        return date_result

    def get_files(self):
        """从文件夹路径获取文件列表"""

        files = []
        # 从文件夹路径获取文件列表,并剔除非docx格式的文件
        for file in os.listdir(self.old_path):
            if file.endswith('.docx') and (not file.startswith('~$')):
                files.append(file)
            else:
                print(file)
                pass

        # self.create(files)

    def save_doc_to_docx(self,files):
        """将doc格式文件转为docx"""
        

    def create(self, files):
        """根据新的文档模板和旧的周报名字创建新的周报文档"""

        for file in files:
            print("%s修改开始" % file)

            # doc = Document(self.template)
            # print(self.old_path+'/'+file)
            print(self.old_path+'/'+file)

            # doc = Document(self.new_path+'/'+file)
            old_doc = Document(self.old_path+'/'+file)

            # self.replace_project_name(old_doc)
            # self.copy(doc, old_doc)

            # old_doc.save(self.old_path+'/'+file)
            # old_doc.save(self.old_path+'/'+file)
            # print("%s修改完成" % file)

    def replace_project_name(self, doc):
        """替换文档里面的项目名字"""

        # 读取所有段落里面的内容并替换
        for p in doc.paragraphs:
            for run in p.runs:
                run.text = run.text.replace('XX', '')
                run.text = run.text.replace('基于微架构的增值业务综合管理系统', project_name)

    def copy(self, doc, old_doc):
        """将旧的周报文档的表格内容依次拷贝到新的周报文档对于位置"""

        # 项目基本信息
        # 项目名称
        doc.tables[0].rows[0].cells[1].text = old_doc.tables[0].rows[0].cells[1].text
        # 报告日期
        doc.tables[0].rows[1].cells[1].text = old_doc.tables[0].rows[1].cells[1].text
        # 报告人
        doc.tables[0].rows[1].cells[3].text = old_doc.tables[0].rows[1].cells[3].text
        # 审批人
        doc.tables[0].rows[1].cells[5].text = old_doc.tables[0].rows[0].cells[3].text

        date = old_doc.tables[0].rows[1].cells[1].text

        d2 = self.next_week(date)
        year = d2.split('年')[0]
        month = int(d2.split('年')[1].split('月')[0])
        day = int(d2.split('月')[1].split('日')[0])
        new_date = '%s年%d月%d日' % (year, month, day)

        # print(timeArray)
        # otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        # print(otherStyleTime+' 00:00:00')
        # d2 = (otherStyleTime +
        #       datetime.timedelta(days=7)).strftime("%Y/%m/%d")
        # print(d2)

        # 项目总体情况描述
        # 本周目标
        doc.tables[1].rows[0].cells[1].text = old_doc.tables[1].rows[0].cells[1].text
        # 当前进展情况
        doc.tables[1].rows[1].cells[1].text = '已完成'

        # 本周计划进展情况
        for i in range(1, len(old_doc.tables[2].rows)):
            if i >= len(doc.tables[2].rows):
                doc.tables[2].add_row()
            # 序号
            doc.tables[2].rows[i].cells[0].text = old_doc.tables[2].rows[i].cells[0].text
            # 计划工作内容
            doc.tables[2].rows[i].cells[1].text = old_doc.tables[2].rows[i].cells[1].text
            # 计划完成时间
            doc.tables[2].rows[i].cells[2].text = old_doc.tables[0].rows[1].cells[1].text
            # 完成进度
            doc.tables[2].rows[i].cells[3].text = '100%'
            # 相关产出
            doc.tables[2].rows[i].cells[4].text = old_doc.tables[2].rows[i].cells[2].text
        # 下周工作计划
        for i in range(1, len(old_doc.tables[3].rows)):
            if i >= len(doc.tables[3].rows):
                doc.tables[3].add_row()
            doc.tables[3].rows[i].cells[0].text = old_doc.tables[3].rows[i].cells[0].text
            doc.tables[3].rows[i].cells[1].text = old_doc.tables[3].rows[i].cells[1].text
            # 计划完成时间
            doc.tables[3].rows[i].cells[2].text = new_date
            doc.tables[3].rows[i].cells[3].text = old_doc.tables[3].rows[i].cells[2].text

        # 需协调事项
        doc.tables[4].rows[1].cells[1].text = '无'


mydoc = Mydocx()
mydoc.get_files()
