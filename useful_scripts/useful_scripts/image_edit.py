
#from PIL import Image

#img =Image.open('semi_nude/semi_nude34.png')
#img.show()

#import matplotlib.pyplot as plt
#img= plt.imread('porn/porn1.png')

#fig, ax = plt.subplots()
#im = ax.imshow(img)

#plt.show()


import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import timedelta
import os
import glob , pickle
import  sys
# Functions and classes for loading and using the Inception model.
#import inception
from PIL import Image
# We use Pretty Tensor to define the new classifier.
#import prettytensor as pt


def get_data(datadir, img_rows , img_cols , crop_tuple=(68,77,1230,714) ):
    # datadir = args.data
    # assume each image is 512x256 split to left and right
    # print(datadir)
    imgs = glob.glob(os.path.join(datadir, '*.png'))
    print(len(imgs))
    # imgs = glob.glob(datadir)
    # print(len(imgs))
    for file in imgs:
        img = Image.open(file)
        width, height = img.size
        if(height > img_rows and width > img_cols):
            # img = img.resize((img_cols, img_rows), Image.LANCZOS)
            img = img.crop(crop_tuple)
            img = img.resize((img_cols, img_rows), Image.NONE)
            img.save(file , optimize=True,quality=95)
    for file in imgs:
        img = Image.open(file)
        img.save( file[:-4]+'.jpg' )
        os.remove(file)
        
def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()
 

 
if __name__ == '__main__':
    get_data('semi_nude', 400 , 600  )


