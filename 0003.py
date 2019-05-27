# 0003
import pymongo
import random
import string

# link mongodb
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['Info']
coupon = db['coupon']
# generate coupon
SelectString = string.ascii_letters+string.digits
for i in range(200):
    result = ''
    for j in range(8):
        result += random.choice(SelectString)
    # insert into database;
    data = {
        'couponid': str(i),
        'couponstring': result
    }
    coupon.insert_one(data)
