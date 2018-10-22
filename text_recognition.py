import pytesseract
import os
import datetime, time

from PIL import Image, ImageEnhance, ImageFilter
from location import Path
from glob import glob

all_images = glob(Path.p + '/*.jpeg')

for image in all_images:
    img_name = image[-21:]
    created_on = os.path.getctime(Path.p + img_name)
    print('Image_Name: ' , img_name, '->',
    'Created On:', datetime.datetime.fromtimestamp(created_on)
                                    .strftime('%m-%d-%Y | %r'))

with open('count.txt','r+') as f:
    value = float(f.read())
    value_int = int(value)
    f.seek(0)
    int_to_str = str(value_int + 1)
    f.write(int_to_str)

image_ = Image.open(Path.p + 'fullsizeoutput_3.jpeg')
image_ = image_.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(image_)
image_ = enhancer.enhance(2)
image_ = image_.convert('1')
image_name = input("Name of Picture: ")
image_.save('viewed_images/' + image_name + '_' + int_to_str + '.jpeg')
text = pytesseract.image_to_string(Image.open('viewed_images/' +
                                   image_name + '_' + int_to_str + '.jpeg'))
data_ = pytesseract.image_to_osd(image_)

print('Image Data: ', data_)
print('___________________________________')
print(text)
