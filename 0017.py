# 0017
from lxml import etree
import xlrd
import os

# 读取文件
def readExcelFile():
    base = os.path.abspath('.')
    df = xlrd.open_workbook(os.path.join(base+'/source/0014', 'student.xls'))
    student = df.sheet_by_name('student')
    
    return student

# 构建文件
def creatXmlFile(xls):
    base = os.path.abspath('.')
    root = etree.Element('root')
    students = etree.Element('students')
    root.append(students)
    comment = etree.Comment('\n\t\t\t\t学生信息表\n\t\t\t\t"id" : [名字, 数学, 语文, 英文]\n\t\t')
    students.insert(-1, comment)
    # 创建字典
    textDict = {}
    for i in range(0, xls.nrows):
        mark = []
        for j in range(1, xls.ncols):
            mark.append(xls.cell(i, j).value)
        textDict[xls.cell(i, 0).value] = mark
    print(textDict)
    students.text = str(textDict)+'\n'

    tree = etree.ElementTree(root)
    tree.write(os.path.join(base+'/source/0014', 'student.xml'), pretty_print=True, xml_declaration=True, encoding='UTF-8')

# 
if __name__ == "__main__":
    xls = readExcelFile()
    creatXmlFile(xls)