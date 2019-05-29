# 0008
from lxml import etree
import requests

# 以一个网站的源代码为例
url = "https://spwii.github.io/about/"
rep = requests.get(url).text
# 解析网页
soup = etree.HTML(rep)
# 找到正文
text = soup.xpath('//*[@id="posts"]/div/div/p/text()')
# 打印正文文本
print(text)


