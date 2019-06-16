# 0004
import re
# open file
file = open('./source/0004/text.txt').read()
# re
pattern = re.compile('[a-zA-Z]+\S*(?=\s)')
# print words in file 
print(len(pattern.findall(file)))