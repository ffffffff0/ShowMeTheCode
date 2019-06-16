# 0011
# open file
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
    segList = jieba.cut_for_search(word)
    # 判断元素
    res = [i for i in list(segList)]
    flag = 0
    for se in res:
        if se in sw:
            print('Freedom')
            flag = 1
            break
    if flag==0:
        print('HumanRight')

    
    
if __name__ == "__main__":
    checkWord()