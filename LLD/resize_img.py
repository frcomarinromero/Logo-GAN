import PIL
import os
import os.path
from PIL import Image

f = r'c://Users/xx/Desktop/imagetest'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((64,64))
    img.save(f_img)