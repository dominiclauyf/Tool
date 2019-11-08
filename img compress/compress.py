from PIL import Image, ImageDraw, ImageFont  #pip install Pillow
import os

print('*** Program Started ***')

diretory=os.listdir()
Image.MAX_IMAGE_PIXELS = 1000000000 
# image_name_input = '05_compress_image_01_input.png'
print(diretory)
for i in diretory:
    if i=='compress.py':
        pass
    else:
        try:
            im = Image.open(i)
            print('Input file name   : ',i)
            size= os.path.getsize (i)
            print('Input Image Size  : ',size)
            if (size>3*1024*1024):#size>20mb
                x=i.split('.')
                image_name_output = x[0]+'compress.'+x[1]
                im.thumbnail((im.size[0]/2,im.size[1]/2),Image.ANTIALIAS)#resize img smaller
                im.save(image_name_output ,optimize=True,quality=30) 
                print('Output file name  : ', image_name_output)
        except Exception as e:
            print(e)
            pass
print('*** Program Ended ***')
input()
    