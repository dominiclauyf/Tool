#pip install pillow
from PIL import Image,ImageDraw,ImageFont 
#font style and size
fnt=ImageFont.truetype('C:\\Windows\\Fonts\\msjh.ttc',18) 
#set img size widthxheight  
img=Image.new('RGB',(1024,3072))
#open file
with open('text.txt',encoding='utf8') as f:                 
    x=f.read()
    d=ImageDraw.Draw(img)
    d.text((10,10),x,font=fnt,fill=(255,255,255))
    #save img name and img type
    img.save('test.png')                                    