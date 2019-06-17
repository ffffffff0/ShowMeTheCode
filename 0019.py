# 0019
# 同0017
from lxml import etree
import xlrd
import os

# 读取文件
def readExcelFile():
    base = os.path.abspath('.')
    df = xlrd.open_workbook(os.path.join(base+'/source/0016', 'numbers.xls'))
    number = df.sheet_by_name('numbers')
    
    return number

# 构建文件
def creatXmlFile(xls):
    base = os.path.abspath('.')
    root = etree.Element('root')
    numbers = etree.Element('numbers')
    root.append(numbers)
    comment = etree.Comment('\n\t\t\t\t数字信息\n\t\t')
    numbers.insert(-1, comment)
    # 创建字典
    textDict = {}
    for i in range(0, xls.nrows):
        mark = []
        for j in range(1, xls.ncols):
            mark.append(xls.cell(i, j).value)
        textDict[xls.cell(i, 0).value] = mark
    print(textDict)
    numbers.text = str(textDict)+'\n'

    tree = etree.ElementTree(root)
    tree.write(os.path.join(base+'/source/0016', 'numbers.xml'), pretty_print=True, xml_declaration=True, encoding='UTF-8')

# 
if __name__ == "__main__":
    xls = readExcelFile()
    creatXmlFile(xls)