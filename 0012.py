# 0012
import os
import jieba

def getStopWord(base):
    sw = []
    # 打开文件
    file = open(os.path.join(base, 'source/0011/filtered_words.txt'), 'r').readlines()
    for word in file:
        sw.append(word.split()[0])
    
    return sw

def checkWord():
    base = os.path.abspath('.')
    sw = getStopWord(base)
    word = input("please input your word:")
    segList = jieba.cut(word)
    res = [i for i in list(segList)]
    # 判断元素
    print(res)
    for se in res:
        if se in sw:
            hx = res[res.index(se)]
            res[res.index(se)] = "*"*len(hx)
    
    print(''.join(res))

if __name__ == "__main__":
    checkWord()