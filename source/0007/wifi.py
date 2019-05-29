import requests

headers = {
    'Origin': 'http://info.zzuli.edu.cn',
    'Referer': 'http://info.zzuli.edu.cn/_t960/2019/0514/c2464a197188/page.htm',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'siteId': '120',
    'type': '2',
    'articleId': '197188'
}

url = "http://info.zzuli.edu.cn/_visitcountdisplay"
requests.get(url, headers=headers, data=data)