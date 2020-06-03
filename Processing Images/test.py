from PIL import Image
import numpy
import imageio
import matplotlib.pyplot as plt
from skimage.io import imshow,show,imread,imsave

"""
from PIL import Image as img
im = img.open('p7.png')
pixels = list(im.getdata())
print(pixels)"""
"""
import scipy.misc
im = scipy.misc.imread('um_000000.png', flatten=False, mode='RGB')
print(im.shape)
for y in range(im.shape[0]):
    for x in range(im.shape[1]):
        color = tuple(im[y][x])
        r, g, b = color
"""
"""
def getPixels(filename):
    img = Image.open(filename, 'r')
    w, h = img.size
    pix = list(img.getdata())
                    
    return [pix[n:n+w] for n in range(0, w*h, w)]

print(getPixels('p7.png'))
"""

#++++++++++++++++++++++++++++++
import cv2
import numpy as np
img=cv2.imread('p4.jpg')
"""
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
print(img)
print("+++++")
print(img[0,0])
print(img.shape)
print(img.shape[0])
print(img.shape[1])
print("=====")
print(img[0,0,0])
print(img[0,0,0])
"""
#print(img[img[0,0]])

#open the original image
pic = imageio.imread('p4.jpg')
imshow(pic,'matplotlib')
show()
#save the image modified 
imsave("/home/alien/Documents/GitHub/Graphics/Processing Images/test_pics/new_1.jpg",pic)
"""
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
"""
"""
def get_image(image_path):
    #Get a numpy array of an image so that one can access values[x][y].
    image = Image.open(image_path, 'r')
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == 'RGB':
        channels = 3
    elif image.mode == 'L':
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values
picture=get_image('p7.png')

print(picture[0,0])
print(picture[0,0,0])
print(picture[0,0,1])
print(picture[0,0,2])
print("++")
print(picture[0,1,0])
print(picture[0,1,1])
print(picture[0,1,2])
print("---")
print(picture[1,1,0])
print(picture[1,1,1])
print(picture[1,1,2])
"""
