
"""
from PIL import Image as img
im = img.open('p4.jpg')
pixels = list(im.getdata())
print(pixels)
"""
"""
from PIL import Image

def getPixels(filename):
    img = Image.open(filename, 'r')
    w, h = img.size
    pix = list(img.getdata())
    return [pix[n:n+w] for n in range(0, w*h, w)]

print(getPixels('p4.jpg'))
"""
import cv2
import numpy as np
img=cv2.imread('p4.jpg')
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
print(img[0,0])