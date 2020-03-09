from PIL import Image
import pytesseract as pyt
import sys
from pdf2image import convert_from_path
import os
import glob
imgs=1
pdf = "Copy_1.pdf"

pages = convert_from_path(pdf,500)

for page in pages:
    file = "page"+str(imgs)+".jpg"
    page.save(file, 'JPEG')

    imgs+=1



limit = imgs-1

output = "out1.txt"

f = open(output,"a")

for i in range(1,limit+1):
    file = "page"+str(i)+".jpg"
    text = str(((pyt.image_to_string(Image.open(file)))))

    text = text.replace('-\n','')
    f.write(text)
f.close()
