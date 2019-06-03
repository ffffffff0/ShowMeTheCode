# 0010
#%%
from skimage import transform as tf
import matplotlib.pyplot as plt 
from PIL import ImageDraw, ImageFont, Image
import numpy as np

#%%
# 生成函数
def creatCaptcha(text, shear=0, size=(60, 24), scale=1):
    # 生成一个图像实例
    im = Image.new("L", size, 'black')
    draw = ImageDraw.Draw(im)
    # 字体
    font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", size=22)
    # 文本
    draw.text((2,2), text, font=font, fill=1)
    # 将PIL图像转为numpy数组
    # 使用skimage 为图像增加错切的效果
    image = np.array(im)
    affine = tf.AffineTransform(shear=shear)
    image = tf.warp(image, affine)

    # 对图像矩阵做归一化,值落在0-1之间
    return image/image.max()


#%%
# 生成一个验证码
captcha = creatCaptcha("TIME", shear=0.3)
plt.imshow(captcha, cmap='Reds')
