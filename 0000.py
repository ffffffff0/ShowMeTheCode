# 0000
from PIL import Image, ImageDraw, ImageFont
import sys

# read the image 
image = Image.open("./source/0000/photo.jpg")
# Draw
draw = ImageDraw.Draw(image)
# font size
font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", size=10)
# write text 
draw.text((320,20), "100", fill="#ff0000")
# save 
image.save("ed.jpg")
