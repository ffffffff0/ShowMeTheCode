# 0006
import os
import re
from collections import Counter
# 统计最重要的单词, 统计单词出现的总次数最大
filepath = "./source/0006"
files = os.listdir(filepath)
# 设置一些不必要的词
stopword = ['and', 'a', 'an', 'or', 'but',
            'to', 'the', 'of', 'is', 'i', 'he', 
            'was', 'as', 'be', 'have', 'has', 'had',
            'also', 'with', 'do', 'done', 'not','into', 
            'on', 'its']
# 统计单词出现的次数


def wordCount(file):
    # 替换一些特殊字符
    prtext = re.sub('[\!\?\'\,;\.\#\"]', '', file.lower()).split()
    prcount = Counter(prtext)
    res = prcount.most_common(len(prcount))
    result = []
    for w in res:
        if w[0] not in stopword:
            result.append(w)
    # 返回结果
    return result

# 统计文件下的文件的单词出现的次数
for file in files:
    f = open(os.path.join(filepath, file)).read()
    print(wordCount(f))
    print("*"*100)
