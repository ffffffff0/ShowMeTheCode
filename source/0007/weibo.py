import requests
import re
import time
import pandas as pd
 
# 把id替换成你想爬的地址id
urls = 'https://m.weibo.cn/api/comments/show?id=4073157046629802&page={}'
 
headers = {'Cookie':'_T_WM=29773866620; MLOGIN=0; WEIBOCN_FROM=1110003030; M_WEIBOCN_PARAMS=uicode%3D10000011%26fid%3D102803; SUB=_2A25x2KSBDeRhGeNI61AQ8ifKzjuIHXVTIszJrDV6PUJbkdAKLVWikW1NSK7nj3ABwXu8yudJT5Q7HWQu4OMoywF9; SUHB=0laFkMXVoHTiJ_; SCF=Au1qlWyyE3xrIocFGV8K45gHGjeBQwA-FoyQ41U3Ht33kzmcamrIo8VlSnhjX9sHIKUC8-cP7zVp7GnSWUGWaGg.; SSOLoginState=1557976273',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
 
# 找到html标签
tags = re.compile('</?\w+[^>]*>')
 
# 设置提取评论function
def get_comment(url):
    j = requests.get(url, headers=headers).json()
    print(j)
    comment_data = j['data']['data']
    for data in comment_data:
        try:
            comment = tags.sub('', data['text']) # 去掉html标签
            reply = tags.sub('', data['reply_text'])
            weibo_id = data['id']
            reply_id = data['reply_id']
            
            comments.append(comment)
            comments.append(reply)
            ids.append(weibo_id)
            ids.append(reply_id)
        except:
            pass
 
 
comments, ids = [], []
for i in range(1, 50):
    url = urls.format(str(i))
    get_comment(url)
    time.sleep(1) # 防止爬得太快被封
 
# 这里我用pandas写入csv文件，需要设置encoding，不然会出现乱码
df = pd.DataFrame({'ID': ids, '评论': comments})
df = df.drop_duplicates()
df.to_csv('data.csv', index=False)

