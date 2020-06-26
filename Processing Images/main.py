
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
"""this one
import cv2
import numpy as np
img=cv2.imread('p4.jpg')
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
print(img[0,1])
"""
#from matplotlib import pyplot as plt
import cv2
img=cv2.imread('pk.PNG')
#================================================================
#>>>>>>>>>>>>>>>>>>>>>>>>>DECLARATIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<

sum1=0
rule_1=0
rule_2=0
sect_a=0
sect_b=0
sect_c=0
sect_d=0
sect_e=0
sect_f=0
sect_g=0
sect_h=0
sect_i=0

ns=9
ns1=3
matrix_savePixel= [[0] * ns for i in range(ns1)]
matrix_saveOperation=[[0] * ns for i in range(ns1)]
#================================================================
#>>>>>>>>>>>>>>>>>>>>>>>>>FUNCTIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def print_mc():
    print("Convolution Mask")
    for row in matrix_convolution:
        print(' '.join([str(elem) for elem in row]))
    

def print_m1():
    for row in matrix_1:
        print(' '.join([str(elem) for elem in row]))
    
def print_m2():
    for row in matrix_2:
        print(' '.join([str(elem) for elem in row]))
    
def print_mk():
    for row in matrix_pre:
        print(' '.join([str(elem) for elem in row]))
    
def print_msp():
    print("matrix savepixel")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    
#================================================================
#>>>>>>>>>>>>>>>>>>>>>>>>sect_h<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelsha(R,G,B,doc):
    #print_mc()
    control=1
    for ixt in range(1,3):
        for iyt in range(3,9):
            #print(" ixt "+str(ixt)+" iyt "+str(iyt))
            if doc==1:
               if 1==control:
                    #print("s1")
                   matrix_savePixel[ixt][iyt]=R
               if 2==control:

                    #print("s2")
                   matrix_savePixel[ixt][iyt]=G
               if 3==control:
                    #print("s3")
                   matrix_savePixel[ixt][iyt]=B
            if doc==2:
                if 4==control:
                    #print("s1")
                    matrix_savePixel[ixt][iyt]=R
                if 5==control:
                    #print("s2")
                    matrix_savePixel[ixt][iyt]=G
                if 6==control:
                    #print("s3")
                    matrix_savePixel[ixt][iyt]=B
            if doc==3:
                if 7==control:
                    #print("s1")
                    matrix_savePixel[ixt][iyt]=R
                if 8==control:
                    #print("s2")
                    matrix_savePixel[ixt][iyt]=G
                if 9==control:
                    #print("s3")
                    matrix_savePixel[ixt][iyt]=B
            if doc==4:
                if 10==control:
                    #print("s1")
                    matrix_savePixel[ixt][iyt]=R
                if 11==control:
                    #print("s2")
                    matrix_savePixel[ixt][iyt]=G
                if 12==control:
                    #print("s3")
                    matrix_savePixel[ixt][iyt]=B
            control = control + 1    
            #matrix_savePixel[ixt][iyt]=1
def save_pixelshb(R,G,B,doc):
    control=1
    for ixt1 in range(3,9):
        if doc==1:

            if 1==control:
                    #print("s1")
                matrix_savePixel[0][ixt1]=R
            if 2==control:
                    #print("s2")
                matrix_savePixel[0][ixt1]=G
            if 3==control:
                    #print("s3")
                matrix_savePixel[0][ixt1]=B
        if doc==2:

            if 4==control:
                    #print("s1"
                matrix_savePixel[0][ixt1]=R
            if 5==control:
                    #print("s2")
                matrix_savePixel[0][ixt1]=G
            if 6==control:
                    #print("s3")
                matrix_savePixel[0][ixt1]=B
        control = control + 1  
        #matrix_savePixel[0][ixt1]=2
def save_pixelshc(R,G,B,doc):
    control=1
    for ixt2 in range(1,3):
        for iyt2 in range(0,3):
            if doc==1:

                if 1==control:
                    #print("s1")
                    matrix_savePixel[ixt2][iyt2]=R
                if 2==control:
                        #print("s2")
                    matrix_savePixel[ixt2][iyt2]=G
                if 3==control:
                        #print("s3")
                    matrix_savePixel[ixt2][iyt2]=B
            if doc==2:

                if 4==control:
                        #print("s1")
                    matrix_savePixel[ixt2][iyt2]=R
                if 5==control:
                        #print("s2")
                    matrix_savePixel[ixt2][iyt2]=G
                if 6==control:
                        #print("s3")
                    matrix_savePixel[ixt2][iyt2]=B
            control = control + 1   
            #print(" ixt "+str(ixt2)+" iyt "+str(iyt2))
            #matrix_savePixel[ixt2][iyt2]=3
def save_pixelshd(R,G,B):
    control=1
    for ixt3 in range(0,3):
        if 1==control:
                    #print("s1")
            matrix_savePixel[0][ixt3]=R
        if 2==control:
                    #print("s2")
            matrix_savePixel[0][ixt3]=G
        if 3==control:
                    #print("s3")
            matrix_savePixel[0][ixt3]=B
        control = control + 1 
        #matrix_savePixel[0][ixt3]=4
#>>>>>>>>>>>>>>>>>>>>>>>>sect_c<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelscA(R,G,B,doc):
    control=1
    for xrt in range(1,3):
        for yrt in range(0,9):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            if doc==4:
                if control==10:
                    matrix_savePixel[xrt][yrt]=R
                if control==11:
                    matrix_savePixel[xrt][yrt]=G
                if control==12:
                    matrix_savePixel[xrt][yrt]=B
            if doc==5:
                if control==13:
                    matrix_savePixel[xrt][yrt]=R
                if control==14:
                    matrix_savePixel[xrt][yrt]=G
                if control==15:
                    matrix_savePixel[xrt][yrt]=B
            if doc==6:
                if control==16:
                    matrix_savePixel[xrt][yrt]=R
                if control==17:
                    matrix_savePixel[xrt][yrt]=G
                if control==18:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelscB(R,G,B,doc):
    control=1
    for xrt in range(9):
        if doc==1:
            if control==1:
                matrix_savePixel[0][xrt]=R
            if control==2:
                matrix_savePixel[0][xrt]=G
            if control==3:
                matrix_savePixel[0][xrt]=B
        if doc==2:
            if control==4:
                matrix_savePixel[0][xrt]=R
            if control==5:
                matrix_savePixel[0][xrt]=G
            if control==6:
                matrix_savePixel[0][xrt]=B
        if doc==3:
            if control==7:
                matrix_savePixel[0][xrt]=R
            if control==8:
                matrix_savePixel[0][xrt]=G
            if control==9:
                matrix_savePixel[0][xrt]=B
        control = control + 1 
#>>>>>>>>>>>>>>>>>>>>>>>>sect_i<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelsiA(R,G,B,doc):
    control=1
    for xrt in range(1,3):
        for yrt in range(0,6):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            if doc==4:
                if control==10:
                    matrix_savePixel[xrt][yrt]=R
                if control==11:
                    matrix_savePixel[xrt][yrt]=G
                if control==12:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelsiB(R,G,B,doc):
    control=1
    for xrt in range(6):
        if doc==1:
            if control==1:
                matrix_savePixel[0][xrt]=R
            if control==2:
                matrix_savePixel[0][xrt]=G
            if control==3:
                matrix_savePixel[0][xrt]=B
        if doc==2:
            if control==4:
                matrix_savePixel[0][xrt]=R
            if control==5:
                matrix_savePixel[0][xrt]=G
            if control==6:
                matrix_savePixel[0][xrt]=B
        control = control + 1 
def save_pixelsiC(R,G,B,doc):
    control=1
    for xrt in range(1,3):
        for yrt in range(6,9):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelsiD(R,G,B):
    control=1
    for ixt3 in range(6,9):
        if 1==control:
                    #print("s1")
            matrix_savePixel[0][ixt3]=R
        if 2==control:
                    #print("s2")
            matrix_savePixel[0][ixt3]=G
        if 3==control:
                    #print("s3")
            matrix_savePixel[0][ixt3]=B
        control = control + 1 
#>>>>>>>>>>>>>>>>>>>>>>>>sect_e<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelseA(R,G,B,doc):
    control=1
    for xrt in range(0,3):
        for yrt in range(3,9):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            if doc==4:
                if control==10:
                    matrix_savePixel[xrt][yrt]=R
                if control==11:
                    matrix_savePixel[xrt][yrt]=G
                if control==12:
                    matrix_savePixel[xrt][yrt]=B
            if doc==5:
                if control==13:
                    matrix_savePixel[xrt][yrt]=R
                if control==14:
                    matrix_savePixel[xrt][yrt]=G
                if control==15:
                    matrix_savePixel[xrt][yrt]=B
            if doc==6:
                if control==16:
                    matrix_savePixel[xrt][yrt]=R
                if control==17:
                    matrix_savePixel[xrt][yrt]=G
                if control==18:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelseB(R,G,B,doc):
    control=1
    for xrt in range(0,3):
        for yrt in range(0,3):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
#>>>>>>>>>>>>>>>>>>>>>>>>sect_b<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelsbA(R,G,B,doc):
    control=1
    for xrt in range(0,3):
        for yrt in range(0,9):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            if doc==4:
                if control==10:
                    matrix_savePixel[xrt][yrt]=R
                if control==11:
                    matrix_savePixel[xrt][yrt]=G
                if control==12:
                    matrix_savePixel[xrt][yrt]=B
            if doc==5:
                if control==13:
                    matrix_savePixel[xrt][yrt]=R
                if control==14:
                    matrix_savePixel[xrt][yrt]=G
                if control==15:
                    matrix_savePixel[xrt][yrt]=B
            if doc==6:
                if control==16:
                    matrix_savePixel[xrt][yrt]=R
                if control==17:
                    matrix_savePixel[xrt][yrt]=G
                if control==18:
                    matrix_savePixel[xrt][yrt]=B
            if doc==7:
                if control==19:
                    matrix_savePixel[xrt][yrt]=R
                if control==20:
                    matrix_savePixel[xrt][yrt]=G
                if control==21:
                    matrix_savePixel[xrt][yrt]=B
            if doc==8:
                if control==22:
                    matrix_savePixel[xrt][yrt]=R
                if control==23:
                    matrix_savePixel[xrt][yrt]=G
                if control==24:
                    matrix_savePixel[xrt][yrt]=B
            if doc==9:
                if control==25:
                    matrix_savePixel[xrt][yrt]=R
                if control==26:
                    matrix_savePixel[xrt][yrt]=G
                if control==27:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
#>>>>>>>>>>>>>>>>>>>>>>>>sect_d<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelsdA(R,G,B,doc):
    control=1
    for xrt in range(0,3):
        for yrt in range(0,6):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            if doc==4:
                if control==10:
                    matrix_savePixel[xrt][yrt]=R
                if control==11:
                    matrix_savePixel[xrt][yrt]=G
                if control==12:
                    matrix_savePixel[xrt][yrt]=B
            if doc==5:
                if control==13:
                    matrix_savePixel[xrt][yrt]=R
                if control==14:
                    matrix_savePixel[xrt][yrt]=G
                if control==15:
                    matrix_savePixel[xrt][yrt]=B
            if doc==6:
                if control==16:
                    matrix_savePixel[xrt][yrt]=R
                if control==17:
                    matrix_savePixel[xrt][yrt]=G
                if control==18:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelsdB(R,G,B,doc):
    control=1
    for xrt in range(0,3):
        for yrt in range(6,9):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
#>>>>>>>>>>>>>>>>>>>>>>>>sect_g<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelsgA(R,G,B,doc):
    control=1
    for ixt in range(0,2):
        for iyt in range(3,9):
            if doc==1:
               if 1==control:
                   matrix_savePixel[ixt][iyt]=R
               if 2==control:
                   matrix_savePixel[ixt][iyt]=G
               if 3==control:
                   matrix_savePixel[ixt][iyt]=B
            if doc==2:
                if 4==control:
                    matrix_savePixel[ixt][iyt]=R
                if 5==control:
                    matrix_savePixel[ixt][iyt]=G
                if 6==control:
                    matrix_savePixel[ixt][iyt]=B
            if doc==3:
                if 7==control:
                    matrix_savePixel[ixt][iyt]=R
                if 8==control:
                    matrix_savePixel[ixt][iyt]=G
                if 9==control:
                    matrix_savePixel[ixt][iyt]=B
            if doc==4:
                if 10==control:
                    matrix_savePixel[ixt][iyt]=R
                if 11==control:
                    matrix_savePixel[ixt][iyt]=G
                if 12==control:
                    matrix_savePixel[ixt][iyt]=B
            control = control + 1   
def save_pixelsgB(R,G,B,doc):
    control=1
    for iyt in range(3,9):
        if doc==1:
            if 1==control:
                matrix_savePixel[2][iyt]=R
            if 2==control:
                matrix_savePixel[2][iyt]=G
            if 3==control:
                matrix_savePixel[2][iyt]=B
        if doc==2:
            if 4==control:
                matrix_savePixel[2][iyt]=R
            if 5==control:
                matrix_savePixel[2][iyt]=G
            if 6==control:
                matrix_savePixel[2][iyt]=B
        control = control + 1   
def save_pixelsgC(R,G,B,doc):
    control=1
    for xrt in range(0,2):
        for yrt in range(0,3):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelsgD(R,G,B):
    control=1
    for ixt3 in range(0,3):
        if 1==control:
            matrix_savePixel[2][ixt3]=R
        if 2==control:
            matrix_savePixel[2][ixt3]=G
        if 3==control:
            matrix_savePixel[2][ixt3]=B
        control = control + 1 
#>>>>>>>>>>>>>>>>>>>>>>>>sect_a<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelsaA(R,G,B,doc):
    control=1
    for xrt in range(0,2):
        for yrt in range(0,9):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            if doc==3:
                if control==7:
                    matrix_savePixel[xrt][yrt]=R
                if control==8:
                    matrix_savePixel[xrt][yrt]=G
                if control==9:
                    matrix_savePixel[xrt][yrt]=B
            if doc==4:
                if control==10:
                    matrix_savePixel[xrt][yrt]=R
                if control==11:
                    matrix_savePixel[xrt][yrt]=G
                if control==12:
                    matrix_savePixel[xrt][yrt]=B
            if doc==5:
                if control==13:
                    matrix_savePixel[xrt][yrt]=R
                if control==14:
                    matrix_savePixel[xrt][yrt]=G
                if control==15:
                    matrix_savePixel[xrt][yrt]=B
            if doc==6:
                if control==16:
                    matrix_savePixel[xrt][yrt]=R
                if control==17:
                    matrix_savePixel[xrt][yrt]=G
                if control==18:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelsaB(R,G,B,doc):
    control=1
    for xrt in range(9):
        if doc==1:
            if control==1:
                matrix_savePixel[2][xrt]=R
            if control==2:
                matrix_savePixel[2][xrt]=G
            if control==3:
                matrix_savePixel[2][xrt]=B
        if doc==2:
            if control==4:
                matrix_savePixel[2][xrt]=R
            if control==5:
                matrix_savePixel[2][xrt]=G
            if control==6:
                matrix_savePixel[2][xrt]=B
        if doc==3:
            if control==7:
                matrix_savePixel[2][xrt]=R
            if control==8:
                matrix_savePixel[2][xrt]=G
            if control==9:
                matrix_savePixel[2][xrt]=B
        control = control + 1 
#>>>>>>>>>>>>>>>>>>>>>>>>sect_f<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixelsfA(R,G,B,doc):
    control=1
    for ixt in range(0,2):
        for iyt in range(0,6):
            if doc==1:
               if 1==control:
                   matrix_savePixel[ixt][iyt]=R
               if 2==control:
                   matrix_savePixel[ixt][iyt]=G
               if 3==control:
                   matrix_savePixel[ixt][iyt]=B
            if doc==2:
                if 4==control:
                    matrix_savePixel[ixt][iyt]=R
                if 5==control:
                    matrix_savePixel[ixt][iyt]=G
                if 6==control:
                    matrix_savePixel[ixt][iyt]=B
            if doc==3:
                if 7==control:
                    matrix_savePixel[ixt][iyt]=R
                if 8==control:
                    matrix_savePixel[ixt][iyt]=G
                if 9==control:
                    matrix_savePixel[ixt][iyt]=B
            if doc==4:
                if 10==control:
                    matrix_savePixel[ixt][iyt]=R
                if 11==control:
                    matrix_savePixel[ixt][iyt]=G
                if 12==control:
                    matrix_savePixel[ixt][iyt]=B
            control = control + 1 
def save_pixelsfB(R,G,B,doc):
    control=1
    for iyt in range(6):
        if doc==1:
            if 1==control:
                matrix_savePixel[2][iyt]=R
            if 2==control:
                matrix_savePixel[2][iyt]=G
            if 3==control:
                matrix_savePixel[2][iyt]=B
        if doc==2:
            if 4==control:
                matrix_savePixel[2][iyt]=R
            if 5==control:
                matrix_savePixel[2][iyt]=G
            if 6==control:
                matrix_savePixel[2][iyt]=B
        control = control + 1 
def save_pixelsfC(R,G,B,doc):
    control=1
    for xrt in range(0,2):
        for yrt in range(6,9):
            if doc==1:
                if control==1:
                    matrix_savePixel[xrt][yrt]=R
                if control==2:
                    matrix_savePixel[xrt][yrt]=G
                if control==3:
                    matrix_savePixel[xrt][yrt]=B
            if doc==2:
                if control==4:
                    matrix_savePixel[xrt][yrt]=R
                if control==5:
                    matrix_savePixel[xrt][yrt]=G
                if control==6:
                    matrix_savePixel[xrt][yrt]=B
            control = control + 1 
def save_pixelsfD(R,G,B):
    control=1
    for ixt3 in range(6,9):
        if 1==control:
            matrix_savePixel[2][ixt3]=R
        if 2==control:
            matrix_savePixel[2][ixt3]=G
        if 3==control:
            matrix_savePixel[2][ixt3]=B
        control = control + 1 
#================================================================
print("Matrix 3 x 3")

n=3
matrix_convolution = [[0] * n for i in range(n)]
matrix_pre = [[0] * n for i in range(n)]#save fraction
#FUNCTIONS
#Fill the matrix
anw=int(input("Any average? yes=1 no=0 "))
if anw == 1:
    numerator=int(input("Numerator: "))
    denominator=int(input("Denominator: "))
    frac=numerator/denominator
    lc=round(frac,2)#get the precision after the decimal point.
    #lc=frac
else:
    lc=1
"""
The [matrix_pre] is to get a float number and multiple it by the original convolution mask[matrix_convolution].
"""
for i in range(n):
    for j in range(n):
        matrix_pre[i][j]=lc

print_mk()

for i in range(n):
    for j in range(n):
        matrix_convolution[i][j]=int(input("Enter number: "))
        print_mc()
for i in range(n):
    for j in range(n):
        matrix_convolution[i][j]=matrix_pre[i][j]*(matrix_convolution[i][j])

print_mc()


n=3
matrix_1=[[0]* n for i in range(n)]#Get the Source pixel 

#matrix_2=[[0]* n for i in range(n)]

for itx in range(img.shape[0]):
    for ity in range(img.shape[1]):
        aux_i=itx
        aux_j=ity

        aux_i3=aux_i4=aux_i
        aux_j3=aux_j4=aux_j

        aux_i3-=1
        aux_j3+=1

        aux_i4+=1
        aux_j4-=1

        aux_i1=aux_i2=aux_i
        aux_j1=aux_j2=aux_j

        aux_i1-=1
        aux_j1-=1
        aux_i2+=1
        aux_j2+=1
        #print("POINT1 [aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+"]  [aux_i "+str(aux_i)+" aux_j "+str(aux_j)+"] [aux_i3 "+str(aux_i3)+" aux_j3 "+str(aux_j3)+"]") 
        #print("POINT2 [aux_i4 "+str(aux_i4)+" aux_j4  "+str(aux_j4)+"] [aux_i "+str(aux_i)+" aux_j "+str(aux_j)+"] [aux_i2 "+str(aux_i2)+" aux_j2  "+str(aux_j2)+"]") 
        rule_1=img.shape[0]
        rule_2=img.shape[1]
        #print_msp()
        #print("rule "+str(rule_1))
        rule_1-=1
        rule_2-=1
        #print("rule1 "+str(rule_1))
        #print("rule2 "+str(rule_2))
        #====================>>       BELOW SIDE      <<===================
        if aux_i2 > rule_1:
            sect_a=1
            sect_b=0
            sect_c=0
            sect_d=0
            sect_e=0
            sect_f=0
            sect_g=0
            sect_h=0
            sect_i=0
        #====================>>       CENTER SIDE      <<==================
        if aux_i2 <= rule_1:
            sect_b=1
            sect_a=0
            sect_c=0
            sect_d=0
            sect_e=0
            sect_f=0
            sect_g=0
            sect_h=0
            sect_i=0
        #====================>>       ABOVE SIDE      <<===================
        if aux_i1<0 :
            sect_a=0
            sect_b=0
            sect_c=1
            sect_d=0
            sect_e=0
            sect_f=0
            sect_g=0
            sect_h=0
            sect_i=0
        #====================>>       RIGHT SIDE      <<===================
        if aux_j2>rule_1:
            sect_b=0
            sect_c=0
            sect_d=1
            sect_e=0
            sect_f=0
            sect_g=0
            sect_h=0
            sect_i=0
        #====================>>       LEFT SIDE      <<====================
        if aux_j1<0:
            sect_b=0
            sect_c=0
            sect_d=0
            sect_e=1
            sect_f=0
            sect_g=0
            sect_h=0
            sect_i=0
        #====================>>BELOW RIGHT SIDE CORNER<<====================
        if aux_i2>rule_1 and aux_j2>rule_1: 
            sect_a=0
            sect_b=0
            sect_c=0
            sect_d=0
            sect_e=0
            sect_f=1
            sect_g=0
            sect_h=0
            sect_i=0
        #====================>>BELOW LEFT SIDE CORNER<<=====================      
        if aux_i4>rule_1 and aux_j4<0: 
            sect_a=0
            sect_b=0
            sect_c=0
            sect_d=0
            sect_e=0
            sect_f=0
            sect_g=1
            sect_h=0
            sect_i=0
        #====================>>ABOVE LEFT SIDE CORNER<<=====================
        if aux_i1<0 and aux_j1<0: 
            sect_h=1 
            sect_g=0
            sect_f=0
            sect_b=0
            sect_d=0
            sect_a=0
            sect_e=0
            sect_c=0 
        #====================>>ABOVE RIGHT SIDE CORNER<<====================
        if aux_i3<0 and aux_j3>rule_1:
            sect_i=1
            sect_h=0
            sect_g=0
            sect_f=0
            sect_b=0
            sect_d=0
            sect_a=0
            sect_e=0
            sect_c=0
        
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>SECTIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        #====================>>ABOVE RIGHT SIDE CORNER<<====================
        if sect_i == 1:
            aux_i3+=1
            aux_j3-=2
            aux_j4+=1
            dist1=1
            #A
            for x in range(aux_i3,aux_i4+1,):
               for y in range(aux_j3,aux_j4+1,):
                   # print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    #sum1+=matrix_1[x][y]
                 #   print("==========="+str(sum1))
                    color= tuple(img[x][y])
                    r, g, b =  color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelsiA(r,g,b,dist1)
                    dist1 = dist1 + 1
                    #print_msp()

               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            dist3=1
            xr3=aux_j3
            while xr3<=rule_1:
                color= tuple(img[rule_1][xr3])
                r,g,b =  color
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(xr3)+"]")
                save_pixelsiB(r,g,b,dist3)
                dist3 = dist3 + 1
                xr3 = xr3 + 1
                #print_msp()
            #C
            dist2=1
            i8=0
            while i8<=aux_i4:
                color= tuple(img[i8][0])
                r,g,b =  color
                #print("Mc")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i8)+","+str(0)+"]")
                save_pixelsiC(r,g,b,dist2)
                dist2 = dist2 + 1
                
                i8 = i8 + 1
                #print_msp()
            #D
            #print("Md") 
            color= tuple(img[rule_1][0])
            r,g,b =  color
            save_pixelsiD(r,g,b)
            #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(rule_2)+"]")
            #print_msp()
            
            #sum1+=matrix_1[rule_1][0]
          #  matrix_2[aux_i][aux_j]=sum1 
        #====================>>ABOVE LEFT SIDE CORNER<<=====================
        if sect_h == 1:
            aux_i1+=1
            aux_j1+=1
            #A
            dit=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                    color = tuple(img[x][y])
                    r, g, b = color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelsha(r,g,b,dit)
                    dit = dit + 1
                    #print_msp()   
            #B
            i7=0
            dit1=1
            while i7<=aux_j2:
                color= tuple(img[rule_1][i7])
                r,g,b =  color
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(i7)+"]")
                save_pixelshb(r,g,b,dit1)
                dit1 = dit1 + 1
                i7 = i7 + 1
                #print_msp()
            #C
            xr2=0
            dit2=1
            while xr2<=aux_j2:
                color= tuple(img[xr2][rule_2])
                r,g,b =  color
                #print("Mc")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(xr2)+","+str(rule_2)+"]")
                save_pixelshc(r,g,b,dit2)
                dit2 = dit2 + 1
                xr2 = xr2 + 1
                #print_msp()
            #D
            #print("Md") 
            color= tuple(img[rule_1][rule_2])
            r,g,b =  color
            save_pixelshd(r,g,b)
            #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(rule_2)+"]")
            #print_msp()   
        #====================>>BELOW LEFT SIDE CORNER<<=====================       
        if sect_g == 1:
            aux_j3-=1
            aux_i4-=1
            aux_j4+=2
            dist8=1
            #A
           # print("++POINT3 [aux_i3 "+str(aux_i3)+" aux_j3 "+str(aux_j3)+"] [aux_i "+str(aux_i)+" aux_j "+str(aux_j)+"] [aux_i4 "+str(aux_i4)+" aux_j4  "+str(aux_j4)+"]") 
            for x in range(aux_i3,aux_i4+1):
                for y in range(aux_j3,aux_j4+1):
                    color= tuple(img[x][y])
                    r, g, b =  color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelsgA(r,g,b,dist8)
                    dist8 = dist8 + 1
                    #print_msp()
             #       print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                   # sum1+=matrix_1[x][y]
            #        print("==========="+str(sum1))
            #B
            ik6=0
            dist9=1
            while ik6<=aux_j4:
              #  print("Mb m "+str(matrix_1[0][ik6])+" x "+str(0)+" y "+str(ik6))
               # sum1+=matrix_1[0][ik6]
               # print("==========="+str(sum1))
                color= tuple(img[0][ik6])
                r, g, b =  color
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(ik6)+"]")
                save_pixelsgB(r,g,b,dist9)
                dist9 = dist9 + 1
                #print_msp()
                ik6 = ik6 + 1
            #C
            it3=aux_i3
            dist10=1
            while it3<=rule_2:
                #print("Mc m "+str(matrix_1[it3][rule_1])+" x "+str(it3)+" y "+str(rule_1))
               # sum1+=matrix_1[it3][rule_1]
                #print("==========="+str(sum1))
                color= tuple(img[it3][rule_2])
                r, g, b =  color
                #print("Mc")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(it3)+","+str(rule_2)+"]")
                save_pixelsgC(r,g,b,dist10)
                dist10 = dist10 + 1
                #print_msp()
                it3 = it3 + 1
           # sum1+=matrix_1[0][rule_1]
            #print("==========="+str(sum1))
           # matrix_2[aux_i][aux_j]=sum1
            #D
            #print("Md") 
            color= tuple(img[0][rule_2])
            r,g,b =  color
            save_pixelsgD(r,g,b)
            #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(rule_2)+"]")
            #print_msp()
        #====================>>BELOW RIGHT SIDE CORNER<<====================       
        if sect_f == 1:
            aux_i2-=1
            aux_j2-=1
            
            #A
            dist20=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
            #        print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    color= tuple(img[x][y])
                    r, g, b =  color
                    print("Ma")
                    print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelsfA(r,g,b,dist20)
                    dist20 = dist20 + 1
                    print_msp()
                    #sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            xr=aux_j1
            dist22=1
            while xr<=rule_1:
                #sum1+=matrix_1[0][xr]
                color= tuple(img[0][xr])
                r, g, b =  color
                print("Mb")
                print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(xr)+"]")
                save_pixelsfB(r,g,b,dist22)
                dist22 = dist22 + 1
                print_msp()
                xr = xr + 1
            
            i5=aux_i1
            dist21=1
            #C
            while i5<=rule_1:
                #sum1+=matrix_1[i5][0]
                color= tuple(img[i5][0])
                r, g, b =  color
                print("Mc")
                print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i5)+","+str(0)+"]")
                save_pixelsfC(r,g,b,dist21)
                dist21 = dist21 + 1
                print_msp()
                i5 = i5 + 1
                
            #sum1+=matrix_1[0][0]
          #  matrix_2[aux_i][aux_j]=sum1
            #D
            print("Md") 
            color= tuple(img[0][0])
            r,g,b =  color
            save_pixelsfD(r,g,b)
            print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(0)+"]")
            print_msp()
        #====================>>       LEFT SIDE      <<==================== 
        if sect_e == 1:
            aux_j1+=1
            #A
            dist4=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
                    #print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    #sum1+=matrix_1[x][y]
                    #print("==========="+str(sum1))
                    color = tuple(img[x][y])
                    r, g, b = color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelseA(r,g,b,dist4)
                    dist4 = dist4 + 1
                    #print_msp() 
         #print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            i4=aux_i1
            dist5=1
            
            while i4<=aux_i2:
                color= tuple(img[i4][rule_2])
                r,g,b =  color
                save_pixelseB(r,g,b,dist5)
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i4)+","+str(rule_2)+"]")
                dist5 = dist5 + 1
                #print_msp() 
                #print("Mb m "+str(matrix_1[i4][rule_1])+" x "+str(i4)+" y "+str(rule_1))
                #sum1+=matrix_1[i4][rule_1]
                #print("==========="+str(sum1))
                i4 = i4 + 1
           # matrix_2[aux_i][aux_j]=sum1
        #====================>>       RIGHT SIDE      <<===================
        if sect_d == 1:
            aux_j2-=1
            dist6=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                    #print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    #sum1+=matrix_1[x][y]
                    #print("==========="+str(sum1))
                    color = tuple(img[x][y])
                    r, g, b = color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelsdA(r,g,b,dist6)
                    dist6 = dist6 + 1
                    #print_msp() 
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            i3=aux_i1
            dist7=1
            while i3<=aux_i2:
                color= tuple(img[i3][0])
                r,g,b =  color
                save_pixelsdB(r,g,b,dist7)
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i3)+","+str(0)+"]")
                dist7 = dist7 + 1
                #print_msp() 
                #print("Mb m "+str(matrix_1[i3][0])+" x "+str(i3)+" y "+str(0))
                #sum1+=matrix_1[i3][0]
                #print("==========="+str(sum1))
                i3 = i3 + 1
           # matrix_2[aux_i][aux_j]=sum1 
        #====================>>       ABOVE SIDE      <<===================
        if sect_c == 1:
            aux_i1+=1
            #A
            dit5=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                   color = tuple(img[x][y])
                   r, g, b = color
                   #print("Ma")
                  # print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                   save_pixelscA(r,g,b,dit5)
                   dit5 = dit5 + 1
                 #  print_msp() 
            #        print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
               #     sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                      
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            dit6=1
            i2=aux_j1
            while i2<=aux_j2:
                color= tuple(img[rule_1][i2])
                r,g,b =  color
                save_pixelscB(r,g,b,dit6)
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(i2)+"]")
                dit6 = dit6 + 1
                # sum1+=matrix_1[rule_1][i2]
                i2 = i2 + 1
                #print_msp()
            #matrix_2[aux_i][aux_j]=sum1
        #====================>>       BELOW SIDE      <<===================
        if sect_a == 1:
            aux_i2-=1
            #A
            dist11=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
                    #print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                #    sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                    color = tuple(img[x][y])
                    r, g, b = color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelsaA(r,g,b,dist11)
                    dist11 = dist11 + 1
                    #print_msp() 
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            ii=aux_j1
            dist12=1
            while ii<=aux_j2:
                #sum1+=matrix_1[0][ii]
                color= tuple(img[0][ii])
                r,g,b =  color
                save_pixelsaB(r,g,b,dist12)
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(ii)+"]")
                dist12 = dist12 + 1
                #print_msp()
                ii = ii + 1
            #matrix_2[aux_i][aux_j]=sum1
        #====================>>       CENTER SIDE      <<==================
        if sect_b == 1:

            
            dist6=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
            #        print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                #    sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                   color = tuple(img[x][y])
                   r, g, b = color
                   #print("Ma")
                   #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                   save_pixelsbA(r,g,b,dist6)
                   dist6 = dist6 + 1
                   #print_msp()
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            #matrix_2[aux_i][aux_j]=sum1
            
           # 
        #clean values
        if sect_a==1 or sect_b==1 or sect_c==1 or sect_d==1 or sect_e==1 or sect_f==1 or sect_g==1 or sect_h==1 or sect_i==1:
            aux_j=0
            aux_i=0
            sum1=0
            sect_b=0
            sect_a=0
            sect_c=0
            sect_d=0
            sect_e=0
            sect_f=0
            sect_g=0
            sect_h=0
            sect_i=0
            #clean matrix
            for clmx in range(3):
                for clmy in range(9):
                    matrix_savePixel[clmx][clmy]=0
            
            #print("Data and matrix cleaned")
#print_m1()
#print_m2()
#print(type(matrix_1))
#print(type(matrix_2))

"""
[      ,      ][      ,      ][      ,      ][aux_i3,aux_j3][      ,      ]
[      ,      ][      ,      ][ aux_i,aux_j ][      ,      ][      ,      ]
[      ,      ][aux_i4,aux_j4][      ,      ][      ,      ][      ,      ]


[      ,      ][aux_i1,aux_j1][      ,      ][      ,      ][      ,      ]
[      ,      ][      ,      ][ aux_i,aux_j ][      ,      ][      ,      ]
[      ,      ][      ,      ][      ,      ][aux_i2,aux_j2][      ,      ]




[      ,      ][aux_i1,aux_j1][      ,      ][aux_i3,aux_j3][      ,      ]
[      ,      ][      ,      ][ aux_i,aux_j ][      ,      ][      ,      ]
[      ,      ][aux_i4,aux_j4][      ,      ][aux_i2,aux_j2][      ,      ]
"""