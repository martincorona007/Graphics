
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
from matplotlib import pyplot as plt
import random
#--------VARIABLES
aux_i=0
aux_j=0
aux_i1=0
aux_j1=0
aux_i2=0
aux_j2=0
sum1=0
rule_1=0

aux_i3=0
aux_j3=0
aux_i4=0
aux_j4=0

sect_a=0
sect_b=0
sect_c=0
sect_d=0
sect_e=0
sect_f=0
sect_g=0
sect_h=0
sect_i=0
#--------FUNCTIONS
#
def print_mc():
    for row in a:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

def print_m1():
    for row in matrix_1:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
def print_m2():
    for row in matrix_2:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
"""

print("Matrix 3 x 3")
n=3
a = [[0] * n for i in range(n)]
#FUNCTIONS
#Fill the matrix
for i in range(n):
    for j in range(n):
        a[i][j]=int(input("Enter number: "))
        print_mc()
"""
n=5
matrix_1=[[0]* n for i in range(n)]
matrix_2=[[0]* n for i in range(n)]

for i in range(0,n,1):
    for j in range(0,n,1):
        matrix_1[i][j]=random.randint(1,40)

for itx in range(n):
    for ity in range(n):
        aux_i=itx
        aux_j=ity

        aux_i3=aux_i4=aux_i
        aux_j3=aux_j4=aux_j

        aux_i3-=1
        aux_j3+=1

        aux_i4+=1
        aux_i42=aux_i4
        aux_j4-=1

        aux_i1=aux_i2=aux_i
        aux_j1=aux_j2=aux_j

        aux_i1-=1
        aux_j1-=1
        aux_i2+=1
        aux_j2+=1
        print("Px aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        print("Pk aux_i4 "+str(aux_i4)+" aux_j1 "+str(aux_j4)+" aux_i3 "+str(aux_i3)+" aux_j3 "+str(aux_j3)) 
        
        rule_1=n
        rule_1-=1

        if aux_i2 > rule_1:
            sect_a=1
        if aux_i2 <= rule_1:
            sect_b=1
        if aux_i1<0 :
            sect_c=1
            sect_b=0
            sect_a=0
        if aux_j2>rule_1:
            sect_d=1
            sect_b=0
          
        if aux_j1<0:
            sect_e=1
            sect_b=0
        if aux_i2>rule_1 and aux_j2>rule_1: 
            sect_f=1
            sect_b=0
            sect_d=0
            sect_a=0
        if aux_i4>rule_1 and aux_j4<0: 
            sect_g=1
            sect_f=0
            sect_b=0
            sect_d=0
            sect_a=0
            sect_e=0
        if aux_i1<0 and aux_j1<0: 
            sect_h=1 
            sect_g=0
            sect_f=0
            sect_b=0
            sect_d=0
            sect_a=0
            sect_e=0
            sect_c=0 
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
        #BELOW SIDE
        if sect_a == 1:
            aux_i2-=1
            x = aux_i1
            y = aux_j1
            while x<=aux_i2:
                while y<=aux_j2:
                    sum1+=matrix_1[x][y] 
                    y = y + 1
                x = x + 1
            ii=aux_j1
            while ii<=aux_j2:
                sum1+=matrix_1[0][ii]
                ii = ii + 1
            matrix_2[aux_i][aux_j]=sum1
        #CENTER SIDE
        if sect_b == 1:
            
            x = aux_i1
            y = aux_j1
            while x<=aux_i2:
                while y<=aux_j2:
                    sum1+=matrix_1[x][y]
                    y = y + 1
                x = x + 1
            matrix_2[aux_i][aux_j]=sum1
            
           # print("==========="+str(sum1))
           # print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
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

print_m1()
print_m2()