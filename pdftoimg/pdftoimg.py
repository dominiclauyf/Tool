from pdf2image import convert_from_path #pip install pdf2image
import os
# (windows) poppler bin\ into path
directory=os.listdir()
for i in directory:
    try:
        x=i.split('.')
        if x[1]=='pdf':
           images = convert_from_path(i)
           for j in images:
                image_name_output=x[0]+"convert.jpg"
                j.save(image_name_output ,optimize=True,quality=100) 
                print(image_name_output)
    except Exception as e:
        print(e)
        pass
input('done,press enter key to continue')
    