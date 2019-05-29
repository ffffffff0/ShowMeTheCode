# 0009
import requests
from lxml import etree

# 依然一个网站为例
url = "https://spwii.github.io/about"
rep = requests.get(url).text
soup = etree.HTML(rep)

# 找到网页源码中所包含的链接
links = soup.xpath('//*/a/@href')
# 打印所有链接完全地址
for link in links:
    if link[0]=='/':
        print(url+link)
    elif link[0]=='#':
        print(url+'/'+link)
    else:
        print(link)