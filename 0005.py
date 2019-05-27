# 00005
import os
from PIL import Image

# set dir
filepath = './source/0005'
files = os.listdir(filepath)
# iter image
for file in files:
    f = Image.open(os.path.join(filepath, file))
    # resize
    resizef = f.resize((1136, 640), Image.ANTIALIAS)
    # save
    resizef.save("r"+file)
    