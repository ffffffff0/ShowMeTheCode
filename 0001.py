# 0001
import random
import string

# coupon length 
length = 8
# letters and numbers
SelectString = string.ascii_letters + string.digits

# iter 
for i in range(200):
    result = ''
    for j in range(length):
        result+=random.choice(SelectString)
    print(result)


