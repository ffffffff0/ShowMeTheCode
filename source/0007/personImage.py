import requests
import os
from threading import Thread
from queue import Queue
import ast
from pymongo import MongoClient


class GetImage(object):
    def __init__(self):
        self.data = {
            # "应用数学": "541510020140",
            "信息计算科学": "541510010140",
            # "高分子材料与工程": "541702030155",
            # "化学工程与工艺(精细化工)": "541704070102",
            # "环境工程": "541604050102",
            # "新能源材料与器件": "541704100101",
            # "应用化学": "541404080160",
            # "电气工程及其自动化": "541701020101",
            # "轨道交通信号与控制": "541701070102",
            # "智能电网信息工程": "541701060108",
            # "自动化": "541701010107",
            # "电子信息工程": "541702010223",
            # "IEC产品设计": "541712270114",
            # "IEC信息工程": "541712250118",
            # "IEC电气工程": "541712260106",
            # "IEC电子商务": "541712030104",
            # "IEC国际商务": "541712280104",
            # "IEC环境设计": "541712270819",
            # "IEC计算机科学与技术(互联网科学与技术)": "541712010101",
            # "IEC数字媒体艺术": "541712270103",
            # "测控技术与仪器": "541702030123",
            # "车辆工程": "541702080102",
            # "机械设计制造及其自动化": "541702010111",
            # "计算机科学与技术": "541701060138",
            # "计算机科学与技术(3G软件)": "541713140103",
            # "计算机科学与技术(嵌入式软件)": "541713430109",
            # "通信工程": "541703040112",
            # "网络工程": "541704010233",
            # "物联网工程": "541703010129",
            # "建筑电气与智能化": "541401040241",
            # "建筑环境与能源应用工程": "541722070104",
            # "财务管理": "541706050139",
            # "电子商务": "541706090103",
            # "工商管理": "541703010142",
            # "会计学": "541503030111",
            # "经济学": "541706020107",
            # "市场营销": "541706050116",
            # "物流管理": "541706060101",
            # "过程装备与控制工程": "541721030103",
            # "能源与动力工程": "541721060101",
            # "软件工程": "541713460101",
            # "生物工程": "541703020106",
            # "食品科学与工程": "541703010137",
            # "食品科学与工程(烟草科学与工程)": "541702030119",
            # "食品质量与安全": "541703040121",
            # "烟草": "541703090108",
            # "朝鲜语": "541708030123",
            # "英语": "541708010111",
            # "材料物理": "541711020102",
            # "电子科学与技术": "541711010112",
            # "产品设计": "541705360106",
            # "服装与服饰设计": "541705360223",
            # "环境设计": "541705361022",
            # "视觉传达设计": "541705360203",
            # "数字媒体艺术": "541705360525",
            # "法学": "541709010111",
            # "公共事业管理": "541709050103",
            # "劳动与社会保障": "541709040115",
            # "工艺美术（陶瓷艺术）": "541705360503"
        }
        self.Infoheaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5,ja-JP;q=0.4,ja;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=900CFFB2853DF75AA8D77AE058F9B5EE',
            'Host': 'sjwj.zzuli.edu.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
        self.Imgheaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5,ja-JP;q=0.4,ja;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'kys.zzuli.edu.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36'
        }
        self.logindata = {
            'stu_id': ''
        }
        self.query_string = {
            'memberId': '',
            'pwd': '{SSHA}lhK1w5rIH9ZP4c60ngEMaNSAUv1QM8wG6RXIVQ=='
        }
        self.qid = Queue()
        self.thread_num = 1
        client = MongoClient("localhost", 27017)
        db = client['Info']
        self.col = db['personinfo']
        self.infoUrl = "http://sjwj.zzuli.edu.cn/dmm_personal/student/paisan/paisanStu"
        self.imgUrl = "http://kys.zzuli.edu.cn/authentication/public/getHeadImg"

    def getName(self):
        while not self.qid.empty():
            ids = self.qid.get()
            self.logindata['stu_id'] = str(ids)
            self.query_string['memberId'] = str(ids)
            inforep = requests.post(
                self.infoUrl, headers=self.Infoheaders, data=self.logindata).text
            imgrep = requests.post(
                self.imgUrl, headers=self.Imgheaders, data=self.query_string)

            try:
                repDict = ast.literal_eval(inforep)
                print(repDict)
                # insert mongodb
                self.col.insert_one(repDict)
                # print("********person info saved!***********")
                # create dir store the image
                sex = repDict['sex']
                major = repDict['major']
                name = repDict['stu_name']
                dept = repDict['dept_name']
                # check image
                imgrep.headers['Transfer-Encoding']
                home = os.path.join(os.path.abspath("."), major)
                # judge dir
                if not os.path.exists(os.path.join(home, sex)):
                    os.makedirs(os.path.join(home, sex))
                else:
                    print("the dir aleardy exists!")
                creatDir = os.path.join(home, sex)
                # save image
                if sex == '女':
                    with open("{}/{}.jpg".format(creatDir, major+"_"+name+"_"+str(ids)), 'wb') as file:
                        file.write(imgrep.content)
                elif sex == '男':
                    with open("{}/{}.jpg".format(creatDir, major+"_"+name+"_"+str(ids)), 'wb') as file:
                        file.write(imgrep.content)
                else:
                    print("No Found the {} sex info!".format(name))
            except:
                print("Something Wrong!")

    def genUrl(self):
        for i, j in self.data.items():
            print("Geting {}!".format(i))
            number = j
            # 541810020140
            # 540910020140
            # 000100000000
            baseId = int(number[0:2]+"09"+number[4:10]+"01")
            baseList = [k for k in range(baseId, baseId+1000000000, 100000000)]
            gradList = [self.qid.put(n)
                        for m in baseList for n in range(m, m+60)]

    def run(self):
        self.genUrl()

        threads = []
        for _ in range(self.thread_num):
            th = Thread(target=self.getName)
            th.start()
            threads.append(th)
        for t in threads:
            t.join()


if __name__ == "__main__":
    info = GetImage()
    info.run()
