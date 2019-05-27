# 0002
import pymysql
import random
import string

# connect the mysql
connection = pymysql.connect(host='localhost', user='root', password='open', db='learn', charset='utf8')
sql = '''INSERT INTO `coupon` (`couponid`, `couponstring`) VALUES (%s, %s)'''
cursor = connection.cursor()
# generate coupon
SelectString = string.ascii_letters+string.digits
length = 8

for i in range(200):
    result = ''
    for j in range(length):
        result+=random.choice(SelectString)
    # insert into table
    cursor.execute(sql, (str(i), result))
    connection.commit()