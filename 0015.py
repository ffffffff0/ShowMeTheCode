# 0015
import pandas as pd 
import os
import ast

def convertFile():
    # 设置目录
    base = os.path.abspath('.')
    text = open(os.path.join(base, 'source/0015/city.txt'), 'r', encoding='UTF-8').read()
    textDict = ast.literal_eval(text)
    for i, j in textDict.items():
        textDict[i]=[j]
    print(textDict)
    # 生成数据框
    df = pd.DataFrame(textDict).T
    print(df)
    # 生成文件
    df.to_excel(os.path.join(base+'/source/0015', 'city.xls'), header=False, sheet_name='city')

if __name__ == "__main__":
    convertFile()