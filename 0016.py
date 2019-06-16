# 0016
import pandas as pd 
import os
import ast


def convertFile():
    base = os.path.abspath('.')
    text = open(os.path.join(base, 'source/0016/numbers.txt'), 'r').read()
    textList = ast.literal_eval(text)
    print(textList)
    # 生成数据框
    df = pd.DataFrame(textList)
    print(df)
    df.to_excel(os.path.join(base+'/source/0016', 'numbers.xls'), header=False, sheet_name='numbers', index=False)
    

if __name__ == "__main__":
    convertFile()