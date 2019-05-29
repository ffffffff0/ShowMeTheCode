# 0007
import re
import os

# 列出程序文件，循环迭代
filepath = './source/0007'
files = os.listdir(filepath)

# 计算程序文件多少行代码，包括空行，注释分别列出


def Count(file):
    blank = 0
    comment = 0
    codeline = 0
    for i in file:
        # 判断空行
        if i in ['\n', '\r\n']:
            blank += 1
        # 判断注释行
        elif i.strip().startswith("#"):
            comment += 1
        # 判断代码行
        else:
            codeline += 1
        # 计算总行数
        allline = blank+comment+codeline
    # 返回结果
    return [blank, comment, codeline, allline]


# 迭代文件
for file in files:
    print(file)
    # 以utf-8的编码格式打开文件
    f = open(os.path.join(filepath, file), 'r', encoding='UTF-8').readlines()
    result = Count(f)
    print("总行数为{}, 空行为{}, 注释为{}, 代码行为{}！".format(
        result[3], result[0], result[1], result[2]))
