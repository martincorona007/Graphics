
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
    print("\n")

def print_m1():
    for row in matrix_1:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
def print_m2():
    for row in matrix_2:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
def print_mk():
    for row in matrix_pre:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
def print_msp():
    print("matrix savepixel")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
#================================================================
#>>>>>>>>>>>>>>>>>>>>>>>>sect_h<<<<<<<<<<<<<<<<<<<<<<<<<
def save_pixel(R,G,B):
    #print_mc()
    control=1
    for ixt in range(1,3):
        for iyt in range(3,9):
            #print(" ixt "+str(ixt)+" iyt "+str(iyt))
            if 1==control:
                #print("s1")
                matrix_savePixel[ixt][iyt]=R
            if 2==control:
                #print("s2")
                matrix_savePixel[ixt][iyt]=G
            if 3==control:
                #print("s3")
                matrix_savePixel[ixt][iyt]=B
            if 4==control:
                #print("s1")
                matrix_savePixel[ixt][iyt]=R
            if 5==control:
                #print("s2")
                matrix_savePixel[ixt][iyt]=G
            if 6==control:
                #print("s3")
                matrix_savePixel[ixt][iyt]=B
            if 7==control:
                #print("s1")
                matrix_savePixel[ixt][iyt]=R
            if 8==control:
                #print("s2")
                matrix_savePixel[ixt][iyt]=G
            if 9==control:
                #print("s3")
                matrix_savePixel[ixt][iyt]=B
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
    #print_mc()
    for ixt1 in range(3,9):
        if 13==control:
                #print("s1")
            matrix_savePixel[0][ixt1]=R
        if 14==control:
                #print("s2")
            matrix_savePixel[0][ixt1]=G
        if 15==control:
                #print("s3")
            matrix_savePixel[0][ixt1]=B
        if 16==control:
                #print("s1"
            matrix_savePixel[0][ixt1]=R
        if 17==control:
                #print("s2")
            matrix_savePixel[0][ixt1]=G
        if 18==control:
                #print("s3")
            matrix_savePixel[0][ixt1]=B
        control = control + 1  
        #matrix_savePixel[0][ixt1]=2
    #print_mc()
    for ixt2 in range(1,3):
        for iyt2 in range(0,3):
            if 19==control:
                #print("s1")
                matrix_savePixel[ixt2][iyt2]=R
            if 20==control:
                    #print("s2")
                matrix_savePixel[ixt2][iyt2]=G
            if 21==control:
                    #print("s3")
                matrix_savePixel[ixt2][iyt2]=B
            if 22==control:
                    #print("s1")
                matrix_savePixel[ixt2][iyt2]=R
            if 23==control:
                    #print("s2")
                matrix_savePixel[ixt2][iyt2]=G
            if 24==control:
                    #print("s3")
                matrix_savePixel[ixt2][iyt2]=B
            control = control + 1   
            #print(" ixt "+str(ixt2)+" iyt "+str(iyt2))
            #matrix_savePixel[ixt2][iyt2]=3
    #print_mc()
    for ixt3 in range(0,3):
        if 25==control:
                    #print("s1")
            matrix_savePixel[0][ixt3]=R
        if 26==control:
                    #print("s2")
            matrix_savePixel[0][ixt3]=G
        if 27==control:
                    #print("s3")
            matrix_savePixel[0][ixt3]=B
        control = control + 1 
        #matrix_savePixel[0][ixt3]=4

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


n=5
matrix_1=[[0]* n for i in range(n)]#Get the Source pixel 

#matrix_2=[[0]* n for i in range(n)]

for itx in range(n):
    for ity in range(n):
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
        print("POINT1 [aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+"] [aux_i "+str(aux_i)+" aux_j "+str(aux_j)+"] [aux_i2 "+str(aux_i2)+" aux_j2  "+str(aux_j2)+"]") 
        print("POINT2 [aux_i3 "+str(aux_i3)+" aux_j3 "+str(aux_j3)+"] [aux_i "+str(aux_i)+" aux_j "+str(aux_j)+"] [aux_i4 "+str(aux_i4)+" aux_j4  "+str(aux_j4)+"]") 
        rule_1=n
        #print("rule "+str(rule_1))
        rule_1-=1
        #print("rule "+str(rule_1))
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
        #====================>>BELOW RIGHT SIDE CONER<<====================
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
        #====================>>BELOW LEFT SIDE CONER<<=====================      
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
        #====================>>ABOVE LEFT SIDE CONER<<=====================
        if aux_i1<0 and aux_j1<0: 
            sect_h=1 
            sect_g=0
            sect_f=0
            sect_b=0
            sect_d=0
            sect_a=0
            sect_e=0
            sect_c=0 
        #====================>>ABOVE RIGHT SIDE CONER<<====================
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
        #====================>>ABOVE RIGHT SIDE CONER<<====================
        if sect_i == 1:
            aux_i3+=1
            aux_j3-=2
            aux_j4+=1
            for x in range(aux_i3,aux_i4+1,):
               for y in range(aux_j3,aux_j4+1,):
                   # print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                 #   print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            i8=0
            while i8<=aux_i4:
                sum1+=matrix_1[i8][0]
                #print("M10b m "+str(matrix_1[i8][0])+" x "+str(i8)+" y "+str(0))
                #print("==========="+str(sum1))
                i8 = i8 + 1
            xr3=aux_j3
            while xr3<=rule_1:
                sum1+=matrix_1[rule_1][xr3]
                #print("M10c m "+str(matrix_1[rule_1][xr3])+" x "+str(rule_1)+" y "+str(xr3))
                #print("==========="+str(sum1))
                xr3 = xr3 + 1
            sum1+=matrix_1[rule_1][0]
          #  matrix_2[aux_i][aux_j]=sum1 
        #====================>>ABOVE LEFT SIDE CONER<<=====================
        if sect_h == 1:
            aux_i1+=1
            aux_j1+=1
            #A
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                  #  print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                 #   print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            i7=0
            while i7<=aux_j2:
                #print("Mb m "+str(matrix_1[rule_1][i7])+" x "+str(rule_1)+" y "+str(i7))
                sum1+=matrix_1[rule_1][i7]
                #print("==========="+str(sum1))
                i7 = i7 + 1
            #C
            xr2=0
            while xr2<=aux_j2:
                #print("Mc m "+str(matrix_1[xr2][aux_j2])+" x "+str(xr2)+" y "+str(aux_j2))
                sum1+=matrix_1[xr2][rule_1]
                #print("==========="+str(sum1))
                xr2 = xr2 + 1
            #D 
            sum1+=matrix_1[rule_1][rule_1]
           # print("==========="+str(sum1))
           # matrix_2[aux_i][aux_j]=sum1
        #====================>>BELOW LEFT SIDE CONER<<=====================       
        if sect_g == 1:
            aux_j3-=1
            aux_i4-=1
            aux_j4+=2
            
           # print("++POINT3 [aux_i3 "+str(aux_i3)+" aux_j3 "+str(aux_j3)+"] [aux_i "+str(aux_i)+" aux_j "+str(aux_j)+"] [aux_i4 "+str(aux_i4)+" aux_j4  "+str(aux_j4)+"]") 
            for x in range(aux_i3,aux_i4+1):
                for y in range(aux_j3,aux_j4+1):
             #       print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
            #        print("==========="+str(sum1))
            ik6=0
            while ik6<=aux_j4:
              #  print("Mb m "+str(matrix_1[0][ik6])+" x "+str(0)+" y "+str(ik6))
                sum1+=matrix_1[0][ik6]
               # print("==========="+str(sum1))
                ik6 = ik6 + 1
            it3=aux_i3
            while it3<=rule_1:
                #print("Mc m "+str(matrix_1[it3][rule_1])+" x "+str(it3)+" y "+str(rule_1))
                sum1+=matrix_1[it3][rule_1]
                #print("==========="+str(sum1))
                it3 = it3 + 1
            sum1+=matrix_1[0][rule_1]
            #print("==========="+str(sum1))
           # matrix_2[aux_i][aux_j]=sum1
        #====================>>BELOW RIGHT SIDE CONER<<====================       
        if sect_f == 1:
            aux_i2-=1
            aux_j2-=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
            #        print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            i5=aux_i1
            while i5<=rule_1:
                sum1+=matrix_1[i5][0]
                i5 = i5 + 1
            xr=aux_j1
            while xr<=rule_1:
                sum1+=matrix_1[0][xr]
                xr = xr + 1
            sum1+=matrix_1[0][0]
          #  matrix_2[aux_i][aux_j]=sum1
        #====================>>       LEFT SIDE      <<==================== 
        if sect_e == 1:
            aux_j1+=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
                    #print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                    #print("==========="+str(sum1))
                    
         #print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            i4=aux_i1
            while i4<=aux_i2:
                #print("Mb m "+str(matrix_1[i4][rule_1])+" x "+str(i4)+" y "+str(rule_1))
                sum1+=matrix_1[i4][rule_1]
                #print("==========="+str(sum1))
                i4 = i4 + 1
           # matrix_2[aux_i][aux_j]=sum1
        #====================>>       RIGHT SIDE      <<===================
        if sect_d == 1:
            aux_j2-=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                    #print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                    #print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            i3=aux_i1
            while i3<=aux_i2:
                #print("Mb m "+str(matrix_1[i3][0])+" x "+str(i3)+" y "+str(0))
                sum1+=matrix_1[i3][0]
                #print("==========="+str(sum1))
                i3 = i3 + 1
           # matrix_2[aux_i][aux_j]=sum1 
        #====================>>       ABOVE SIDE      <<===================
        if sect_c == 1:
            aux_i1+=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
            #        print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            i2=aux_j1
            while i2<=aux_j2:
                sum1+=matrix_1[rule_1][i2]
                i2 = i2 + 1
            #matrix_2[aux_i][aux_j]=sum1
        #====================>>       BELOW SIDE      <<===================
        if sect_a == 1:
            aux_i2-=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
            #        print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            ii=aux_j1
            while ii<=aux_j2:
                sum1+=matrix_1[0][ii]
                ii = ii + 1
            #matrix_2[aux_i][aux_j]=sum1
        #====================>>       CENTER SIDE      <<==================
        if sect_b == 1:
            
            #x = aux_i1
           # y = aux_j1
           # print("in==========="+str(aux_i2))
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
            #        print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                    sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
                    
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
        
            #matrix_2[aux_i][aux_j]=sum1
            
           # 
            
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