# 0014
import pandas as pd 
import os
import ast

def convertFile():
    # 设置目录
    base = os.path.abspath('.')
    text = open(os.path.join(base, 'source/0014/student.txt'), 'r', encoding='UTF-8').read()
    textDict = ast.literal_eval(text)
    print(textDict)
    # 生成数据框
    df = pd.DataFrame(textDict).T
    # 生成文件
    df.to_excel(os.path.join(base+'/source/0014', 'student.xls'), header=False, sheet_name='student')
    print(df)


if __name__ == "__main__":
    convertFile()