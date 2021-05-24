"""
Author: Martin Corona
"""
import cv2
import numpy as np
from PIL import Image
img = cv2.imread('images/prueba2.png')
#>>>>>>>>>>>>>>>>>>>>>>>>>DECLARATIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<

sum1 = 0
rule_1 = 0
rule_2 = 0
sect_a = 0 
sect_b = 0
sect_c = 0
sect_d = 0
sect_e = 0
sect_f = 0
sect_g = 0
sect_h = 0
sect_i = 0

ns = 9
ns1 = 3
matrix_savePixel = [[0] * ns for i in range(ns1)]
matrix_saveOperation =[[0] * ns for i in range(ns1)]
#>>>>>>>>>>>>>>>>>>>>>>>>>FUNCTIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#prints
def print_mc():
    print("Convolution Mask")
    for row in matrix_convolution:
        print(' '.join([str(elem) for elem in row]))

def print_so():
    print("matrix_saveOperation")
    for row in matrix_saveOperation:
        print(' '.join([str(elem) for elem in row]))
    
def print_mk():
    print("matrix_pre")
    for row in matrix_pre:
        print(' '.join([str(elem) for elem in row]))
    
def print_msp():
    print("matrix savepixel")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))

def save_pixelA(R,G,B,doc,a,b,c,d):
    control=1
    for x in range(a,b):
        for y in range(c,d):
            if doc == 1:
               if 1 == control:
                   matrix_savePixel[x][y] = R
               if 2 == control:
                   matrix_savePixel[x][y] = G
               if 3 == control:
                   matrix_savePixel[x][y] = B
            if doc == 2:
                if 4 == control:
                    matrix_savePixel[x][y] = R
                if 5 == control:
                    matrix_savePixel[x][y] = G
                if 6==control:
                    matrix_savePixel[x][y] = B
            if doc == 3:
                if 7 == control:
                    matrix_savePixel[x][y] = R
                if 8 == control:
                    matrix_savePixel[x][y] = G
                if 9 == control:
                    matrix_savePixel[x][y] = B
            if doc == 4:
                if 10 == control:
                    matrix_savePixel[x][y] = R
                if 11 == control:
                    matrix_savePixel[x][y] = G
                if 12 == control:
                    matrix_savePixel[x][y] = B
            control = control + 1
def save_pixelB(R,G,B,doc,a,b,c,d):
    control = 1
    for x in range(a,b):
        for y in range(c,d):
            if doc == 1:
                if control == 1:
                    matrix_savePixel[x][y] = R
                if control == 2:
                    matrix_savePixel[x][y] = G
                if control == 3:
                    matrix_savePixel[x][y] = B
            if doc == 2:
                if control == 4:
                    matrix_savePixel[x][y] = R
                if control == 5:
                    matrix_savePixel[x][y] = G
                if control == 6:
                    matrix_savePixel[x][y] = B
            if doc == 3:
                if control == 7:
                    matrix_savePixel[x][y] = R
                if control == 8:
                    matrix_savePixel[x][y] = G
                if control == 9:
                    matrix_savePixel[x][y] = B
            if doc == 4:
                if control == 10:
                    matrix_savePixel[x][y] = R
                if control == 11:
                    matrix_savePixel[x][y] = G
                if control == 12:
                    matrix_savePixel[x][y] = B
            if doc == 5:
                if control == 13:
                    matrix_savePixel[x][y] = R
                if control == 14:
                    matrix_savePixel[x][y] = G
                if control == 15:
                    matrix_savePixel[x][y] = B
            if doc == 6:
                if control == 16:
                    matrix_savePixel[x][y] = R
                if control == 17:
                    matrix_savePixel[x][y] = G
                if control == 18:
                    matrix_savePixel[x][y] =B
            control = control + 1 
def save_pixelC(R,G,B,doc,a,b,c,d):
    control = 1
    for x in range(a,b):
        for y in range(c,d):
            if doc == 1:
                if control == 1:
                    matrix_savePixel[x][y] = R
                if control == 2:
                    matrix_savePixel[x][y] = G
                if control == 3:
                    matrix_savePixel[x][y] = B
            if doc == 2:
                if control == 4:
                    matrix_savePixel[x][y] = R
                if control == 5:
                    matrix_savePixel[x][y] = G
                if control == 6:
                    matrix_savePixel[x][y] = B
            control = control + 1
def save_pixelD(R,G,B,doc,a,b,c,d):
    control = 1
    for x in range(a,b):
        for y in range(c,d):
            if doc == 1:
                if control == 1:
                    matrix_savePixel[x][y] = R
                if control == 2:
                    matrix_savePixel[x][y] = G
                if control == 3:
                    matrix_savePixel[x][y] = B
            if doc == 2:
                if control == 4:
                    matrix_savePixel[x][y] = R
                if control == 5:
                    matrix_savePixel[x][y] = G
                if control == 6:
                    matrix_savePixel[x][y] = B
            if doc == 3:
                if control == 7:
                    matrix_savePixel[x][y] = R
                if control == 8:
                    matrix_savePixel[x][y] = G
                if control == 9:
                    matrix_savePixel[x][y] = B
            if doc == 4:
                if control == 10:
                    matrix_savePixel[x][y] = R
                if control == 11:
                    matrix_savePixel[x][y] = G
                if control == 12:
                    matrix_savePixel[x][y] = B
            if doc == 5:
                if control == 13:
                    matrix_savePixel[x][y] = R
                if control == 14:
                    matrix_savePixel[x][y] = G
                if control == 15:
                    matrix_savePixel[x][y] = B
            if doc == 6:
                if control == 16:
                    matrix_savePixel[x][y] = R
                if control == 17:
                    matrix_savePixel[x][y] = G
                if control == 18:
                    matrix_savePixel[x][y] = B
            control = control + 1
def save_pixelE(R,G,B,doc,a,b,c,d):
    control = 1
    for x in range(a,b):
        for y in range(c,d):
            if doc == 1:
                if control == 1:
                    matrix_savePixel[x][y] = R
                if control == 2:
                    matrix_savePixel[x][y] = G
                if control == 3:
                    matrix_savePixel[x][y] = B
            if doc == 2:
                if control == 4:
                    matrix_savePixel[x][y] = R
                if control == 5:
                    matrix_savePixel[x][y] = G
                if control == 6:
                    matrix_savePixel[x][y] = B
            if doc == 3:
                if control == 7:
                    matrix_savePixel[x][y] = R
                if control == 8:
                    matrix_savePixel[x][y] = G
                if control == 9:
                    matrix_savePixel[x][y] = B
            control = control + 1  
def save_pixelF(R,G,B,doc,x):
    control = 1
    for y in range(9):
        if doc == 1:
            if control == 1:
                matrix_savePixel[x][y] = R
            if control == 2:
                matrix_savePixel[x][y] = G
            if control == 3:
                matrix_savePixel[x][y] = B
        if doc == 2:
            if control == 4:
                matrix_savePixel[x][y] = R
            if control == 5:
                matrix_savePixel[x][y] = G
            if control == 6:
                matrix_savePixel[x][y] = B
        if doc == 3:
            if control == 7:
                matrix_savePixel[x][y] = R
            if control == 8:
                matrix_savePixel[x][y] = G
            if control == 9:
                matrix_savePixel[x][y] = B
        control = control + 1 
def save_pixelG(R,G,B,doc,x,a,b):
    control = 1
    for y in range(a,b):
        if doc == 1:
            if 1 == control:
                matrix_savePixel[x][y] = R
            if 2 == control:
                matrix_savePixel[x][y] = G
            if 3 == control:
                matrix_savePixel[x][y] = B
        if doc == 2:
            if 4 == control:
                matrix_savePixel[x][y] = R
            if 5 == control:
                matrix_savePixel[x][y] = G
            if 6 == control:
                matrix_savePixel[x][y] = B
        control = control + 1     
def save_pixelH(R,G,B,x,a,b):
    control = 1
    for y in range(a,b):
        if control == 1:
            matrix_savePixel[x][y] = R
        if control == 2:
            matrix_savePixel[x][y] = G
        if control == 3:
            matrix_savePixel[x][y] = B
        control = control + 1  
def save_pixelsbA(R,G,B,doc):
    control = 1
    for x in range(0,3):
        for y in range(0,9):
            if doc == 1:
                if control == 1:
                    matrix_savePixel[x][y] = R
                if control == 2:
                    matrix_savePixel[x][y] = G
                if control == 3:
                    matrix_savePixel[x][y] = B
            if doc == 2:
                if control == 4:
                    matrix_savePixel[x][y] = R
                if control == 5:
                    matrix_savePixel[x][y] = G
                if control == 6:
                    matrix_savePixel[x][y] = B
            if doc == 3:
                if control == 7:
                    matrix_savePixel[x][y] = R
                if control == 8:
                    matrix_savePixel[x][y] = G
                if control == 9:
                    matrix_savePixel[x][y] = B
            if doc == 4:
                if control == 10:
                    matrix_savePixel[x][y] = R
                if control == 11:
                    matrix_savePixel[x][y] = G
                if control == 12:
                    matrix_savePixel[x][y] = B
            if doc == 5:
                if control == 13:
                    matrix_savePixel[x][y] = R
                if control == 14:
                    matrix_savePixel[x][y] = G
                if control == 15:
                    matrix_savePixel[x][y] = B
            if doc == 6:
                if control == 16:
                    matrix_savePixel[x][y] = R
                if control == 17:
                    matrix_savePixel[x][y] = G
                if control == 18:
                    matrix_savePixel[x][y] = B
            if doc == 7:
                if control == 19:
                    matrix_savePixel[x][y] = R
                if control == 20:
                    matrix_savePixel[x][y] = G
                if control == 21:
                    matrix_savePixel[x][y] = B
            if doc == 8:
                if control == 22:
                    matrix_savePixel[x][y] = R
                if control == 23:
                    matrix_savePixel[x][y] = G
                if control == 24:
                    matrix_savePixel[x][y] = B
            if doc == 9:
                if control == 25:
                    matrix_savePixel[x][y] = R
                if control == 26:
                    matrix_savePixel[x][y] = G
                if control == 27:
                    matrix_savePixel[x][y] = B
            control = control + 1 

#>>>>>>>>>>>>>>>>>>>>>>>>OPERARTION<<<<<<<<<<<<<<<<<<<<<<<<<
def operation():
    listnewpixel = []
    sector = 1
    for li in range(3):
        for lo in range(9):
            if sector == 1:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][0])
            if sector == 2:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][0])
            if sector == 3:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][0])
            if sector == 4:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][1])
            if sector == 5:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][1])
            if sector == 6:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][1])
            if sector == 7:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][2])
            if sector == 8:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][2])
            if sector == 9:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[0][2])
            if sector == 10:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][0])
            if sector == 11:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][0])
            if sector == 12:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][0])
            if sector == 13:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][1])
            if sector == 14:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][1])
            if sector == 15:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][1])
            if sector == 16:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][2])
            if sector == 17:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][2])
            if sector == 18:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[1][2])
            if sector == 19:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][0])
            if sector == 20:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][0])
            if sector == 21:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][0])
            if sector == 22:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][1])
            if sector == 23:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][1])
            if sector == 24:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][1])
            if sector == 25:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][2])
            if sector == 26:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][2])
            if sector == 27:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]* matrix_convolution[2][2])
            
            sector = sector + 1

            #print(" itli "+str(itli)+" itlo "+str(itlo))
    #print_so()
    #remove negative numbers
    for clx in range(3):
        for cly in range(9):
            if matrix_saveOperation[clx][cly] < 0:
                matrix_saveOperation[clx][cly] = matrix_saveOperation[clx][cly]*-1
    print_so()
    R = 0
    G = 0
    B = 0
    for oxl in range(3):
        R += matrix_saveOperation[oxl][0] + matrix_saveOperation[oxl][3] + matrix_saveOperation[oxl][6]
        G += matrix_saveOperation[oxl][1] + matrix_saveOperation[oxl][4] + matrix_saveOperation[oxl][7]
        B += matrix_saveOperation[oxl][2] + matrix_saveOperation[oxl][5] + matrix_saveOperation[oxl][8]
    
    print("1p R "+str(R)+" G "+str(G)+" B "+str(B))
    if bias == 1:
        print("with bias")
        if R >= biasv:
            R = biasv
        if G >= biasv:
            G = biasv
        if B >= biasv:
            B = biasv
    else:
        print("without bias")
        if R >= 255:
            R = 255
        if G >= 255:
            G = 255
        if B >= 255:
            B = 255
        if R < 0:
            R = 0
        if G < 0:
            G = 0
        if B < 0:
            B = 0
             #print("1p R "+str(R)+" G "+str(G)+" B "+str(B))
    print("2p R "+str(R)+" G "+str(G)+" B "+str(B))
    saveNP = [R,G,B]
    listnewpixel.append(saveNP)
    return listnewpixel
#================================================================

print("Matrix 3 x 3")

n = 3
matrix_convolution = [[0] * n for i in range(n)]
matrix_pre = [[0] * n for i in range(n)]#save fraction
#FUNCTIONS
#Fill the matrix
anw = int(input("Any average? yes=1 no=0 "))
if anw == 1:
    numerator = int(input("Numerator: "))
    denominator = int(input("Denominator: "))
    frac = numerator / denominator
    lc = round(frac,2)#get the precision after the decimal point.
else:
    lc = 1
anws = int(input("Do you want bias? yes=1 no=0 "))
if anws == 1:
    bias = 1
    anwsr = int(input("Number bias: "))
    biasv = anwsr
else:
    bias = 0
"""
The [matrix_pre] is to get a float number and multiple it by the original convolution mask[matrix_convolution].
"""
for i in range(n):
    for j in range(n):
        matrix_pre[i][j] = lc
        
#print_mk()
print("Convolution Mask")
for i in range(n):
    for j in range(n):
        matrix_convolution[i][j] = int(input("Enter number: "))
        print_mc()
for i in range(n):
    for j in range(n):
        matrix_convolution[i][j] = matrix_pre[i][j] * (matrix_convolution[i][j])

print_mc()

n = 3
matrix_1 = [[0]* n for i in range(n)]#Get the Source pixel 

#matrix_2=[[0]* n for i in range(n)]
#width, height= img.size
width = img.shape[1]
height = img.shape[0]

outputImg = np.zeros([height,width,3],dtype=np.uint8)

for itx in range(height):
    for ity in range(width):
        """
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        +[      ,      ][      ,      ][      ,      ][aux_i3,aux_j3][      ,      ]+
        +[      ,      ][      ,      ][ aux_i,aux_j ][      ,      ][      ,      ]+
        +[      ,      ][aux_i4,aux_j4][      ,      ][      ,      ][      ,      ]+
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        +[      ,      ][aux_i1,aux_j1][      ,      ][      ,      ][      ,      ]+
        +[      ,      ][      ,      ][ aux_i,aux_j ][      ,      ][      ,      ]+
        +[      ,      ][      ,      ][      ,      ][aux_i2,aux_j2][      ,      ]+
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        +[      ,      ][aux_i1,aux_j1][      ,      ][aux_i3,aux_j3][      ,      ]+
        +[      ,      ][      ,      ][ aux_i,aux_j ][      ,      ][      ,      ]+
        +[      ,      ][aux_i4,aux_j4][      ,      ][aux_i2,aux_j2][      ,      ]+
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
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
        print("POINT [aux_i "+str(aux_i)+" aux_j "+str(aux_j)+"]") 
        rule_1=height
        rule_2=width
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
        #====================>>ABOVE LEFT SIDE CORNER<<=====================
        if sect_h == 1:
            aux_i1+=1
            aux_j1+=1
            #A
            ith_1=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                    color = tuple(img[x][y])
                    r, g, b = color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelA(r,g,b,ith_1,1,3,3,9)
                    ith_1 = ith_1 + 1
                    #print_msp()   
            #B
            ih1=0
            dit1=1
            while ih1<=aux_j2:
                color= tuple(img[rule_1][ih1])
                r,g,b =  color
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(i7)+"]")
                save_pixelG(r,g,b,dit1,0,3,9)
                dit1 = dit1 + 1
                ih1 = ih1 + 1
                #print_msp()
            #C
            ih2=0
            dit2=1
            while ih2<=aux_j2:
                color= tuple(img[ih2][rule_2])
                r,g,b =  color
                #print("Mc")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(xr2)+","+str(rule_2)+"]")
                save_pixelC(r,g,b,dit2,1,3,0,3)
                dit2 = dit2 + 1
                ih2 = ih2 + 1
                #print_msp()
            #D
            #print("Md") 
            color= tuple(img[rule_1][rule_2])
            r,g,b =  color
            save_pixelH(r,g,b,0,0,3)
            #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(rule_2)+"]")
            #print_msp()
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
        #====================>>       ABOVE SIDE      <<===================
        if sect_c == 1:
            aux_i1+=1
            #A
            dit5=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                   if y>=width:
                       y = y - 1
                      # print("1POINTP ["+str(x)+","+str(y)+"]")
                       color = tuple(img[x][y])
                       r, g, b = color
                       #print("Ma")
                       # print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                       save_pixelA(r,g,b,dit5,1,3,0,9)
                       dit5 = dit5 + 1
                   else:
                       #print("2POINTP ["+str(x)+","+str(y)+"]")
                       color = tuple(img[x][y])
                       r, g, b = color
                       #print("Ma")
                       # print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                       save_pixelA(r,g,b,dit5,1,3,0,9)
                       dit5 = dit5 + 1
                    #  print_msp() 
                    #  print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
            #B
            dit6=1
            i2=aux_j1
            while i2<=aux_j2:
                if i2>=width:
                    i2 = i2 - 1
                    color= tuple(img[rule_1][i2])
                    r,g,b =  color
                    save_pixelF(r,g,b,dit6,0)
                    #print("Mb")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(i2)+"]")
                    dit6 = dit6 + 1
                    # sum1+=matrix_1[rule_1][i2]
                    i2=aux_j2
                else:
                    color= tuple(img[rule_1][i2])
                    r,g,b =  color
                    save_pixelF(r,g,b,dit6,0)
                    #print("Mb")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(i2)+"]")
                    dit6 = dit6 + 1
                    # sum1+=matrix_1[rule_1][i2]
                i2 = i2 + 1
                    #print_msp()
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
  
        #====================>>ABOVE RIGHT SIDE CORNER<<====================
        if sect_i == 1:
            aux_i3+=1
            aux_j3-=2
            aux_j4+=1
            it_1=1
            #A
            for x in range(aux_i3,aux_i4+1,):
               for y in range(aux_j3,aux_j4+1,):
                    color= tuple(img[x][y])
                    r, g, b =  color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelA(r,g,b,it_1,1,3,0,6)
                    it_1 = it_1 + 1
                    #print_msp()

               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            it_2=1
            xr3=aux_j3
            while xr3<=rule_1:
                color= tuple(img[rule_1][xr3])
                r,g,b =  color
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(rule_1)+","+str(xr3)+"]")
                save_pixelG(r,g,b,it_2,0,0,6)
                it_2 = it_2 + 1
                xr3 = xr3 + 1
                #print_msp()
            #C
            it_3=1
            i1=0
            while i1<=aux_i4:
                color= tuple(img[i1][0])
                r,g,b =  color
                #print("Mc")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i8)+","+str(0)+"]")
                save_pixelC(r,g,b,it_3,1,3,6,9)
                it_3 = it_3 + 1
                i1 = i1 + 1
                #print_msp()
            #D            
            color= tuple(img[rule_1][0])
            r,g,b =  color
            save_pixelH(r,g,b,0,6,9)
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
              
        #====================>>       LEFT SIDE      <<==================== 
        if sect_e == 1:
            aux_j1+=1
            #A
            dist4=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
                    color = tuple(img[x][y])
                    r, g, b = color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelD(r,g,b,dist4,0,3,3,9)
                    dist4 = dist4 + 1
                    #print_msp() 
      
            #B
            i4=aux_i1
            dist5=1
            
            while i4<=aux_i2:
                color= tuple(img[i4][rule_2])
                r,g,b =  color
                save_pixelE(r,g,b,dist5,0,3,0,3)
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i4)+","+str(rule_2)+"]")
                dist5 = dist5 + 1
                #print_msp() 
                #print("Mb m "+str(matrix_1[i4][rule_1])+" x "+str(i4)+" y "+str(rule_1))
                #sum1+=matrix_1[i4][rule_1]
                #print("==========="+str(sum1))
                i4 = i4 + 1
           # matrix_2[aux_i][aux_j]=sum1
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
            
        #====================>>       CENTER SIDE      <<==================
        if sect_b == 1:     
            dist6=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
                    if y==width:
                        y = y - 1
                        color = tuple(img[x][y])
                        r, g, b = color
                        #print("Ma")
                        #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                        save_pixelsbA(r,g,b,dist6)
                        dist6 = dist6 + 1
                    else:
                        color = tuple(img[x][y])
                        r, g, b = color
                        #print("Ma")
                        #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                        save_pixelsbA(r,g,b,dist6)
                        dist6 = dist6 + 1
                        #print_msp()      
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
        #====================>>       RIGHT SIDE      <<===================
        if sect_d == 1:
            aux_j2-=1
            dist6=1
            for x in range(aux_i1,aux_i2+1,):
               for y in range(aux_j1,aux_j2+1,):
                    color = tuple(img[x][y])
                    r, g, b = color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelD(r,g,b,dist6,0,3,0,6)
                    dist6 = dist6 + 1
                    #print_msp()         
            i3=aux_i1
            dist7=1
            while i3<=aux_i2:
                color= tuple(img[i3][0])
                r,g,b =  color
                save_pixelE(r,g,b,dist7,0,3,6,9)
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i3)+","+str(0)+"]")
                dist7 = dist7 + 1
                #print_msp() 
                #print("Mb m "+str(matrix_1[i3][0])+" x "+str(i3)+" y "+str(0))
                #sum1+=matrix_1[i3][0]
                #print("==========="+str(sum1))
                i3 = i3 + 1

            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
                   
        #====================>>BELOW LEFT SIDE CORNER<<=====================       
        if sect_g == 1:
            aux_j3-=1
            aux_i4-=1
            aux_j4+=2
            dist8=1
            #A
            for x in range(aux_i3,aux_i4+1):
                for y in range(aux_j3,aux_j4+1):
                    color= tuple(img[x][y])
                    r, g, b =  color
                    #print("Ma")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelA(r,g,b,dist8,0,2,3,9)
                    dist8 = dist8 + 1
                    #print_msp()
             #       print("Ma m "+str(matrix_1[x][y])+" x "+str(x)+" y "+str(y))
                   # sum1+=matrix_1[x][y]
            #        print("==========="+str(sum1))
            #B
            ik6=0
            dist9=1
            while ik6<=aux_j4:
                color= tuple(img[0][ik6])
                r, g, b =  color
                #print("Mb")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(ik6)+"]")
                save_pixelG(r,g,b,dist9,2,3,9)
                dist9 = dist9 + 1
                #print_msp()
                ik6 = ik6 + 1
            #C
            it3=aux_i3
            dist10=1
            #  print("height "+str(height))
            while it3<=rule_2:
                
                if it3>=height:
                    it3 = it3 - 1
                    color= tuple(img[it3][rule_2])
                    r, g, b =  color
                    #print("Mc")
                    #print("1<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(it3)+","+str(rule_2)+"]")
                    save_pixelC(r,g,b,dist10,0,2,0,3)
                    dist10 = dist10 + 1
                    it3 = rule_2
                else:    
                    color= tuple(img[it3][rule_2])
                    r, g, b =  color
                    #print("Mc")
                    #             print("2<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(it3)+","+str(rule_2)+"]")
                    save_pixelC(r,g,b,dist10,0,2,0,3)
                    dist10 = dist10 + 1
                    #print_msp()
                it3 = it3 + 1
                
            #D
            #print("Md") 
            color= tuple(img[0][rule_2])
            r,g,b =  color
            save_pixelH(r,g,b,2,0,3)
            #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(rule_2)+"]")
            #print_msp()
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
            
        #====================>>       BELOW SIDE      <<===================
        if sect_a == 1:
            aux_i2-=1
            #A
            dist11=1
            for x in range(aux_i1,aux_i2+1,):
                for y in range(aux_j1,aux_j2+1,):
                    if y==width:
                        y = y - 1
                        color = tuple(img[x][y])
                        r, g, b = color
                        #print("Ma")
                        #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                        save_pixelB(r,g,b,dist11,0,2,0,9)
                        dist11 = dist11 + 1    
                    else:
                        color = tuple(img[x][y])
                        r, g, b = color
                        #print("Ma")
                        #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                        save_pixelB(r,g,b,dist11,0,2,0,9)
                        dist11 = dist11 + 1
                        #print_msp() 
               # print("==========="+str(sum1))
              #  print("APK aux_i1 "+str(aux_i1)+" aux_j1 "+str(aux_j1)+" aux_i2 "+str(aux_i2)+" aux_j2 "+str(aux_j2)) 
            #B
            ii=aux_j1
            dist12=1
            #print(" POINT [ii"+str(ii)+",aux_j2"+str(aux_j2)+"]")
            while ii<=aux_j2:
                if ii>=width:
                    ii = ii - 1
                    color= tuple(img[0][ii])
                    r,g,b =  color
                    save_pixelF(r,g,b,dist12,2)
                    #print("Mb")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(ii)+"]")
                    dist12 = dist12 + 1
                    ii=aux_j2
                else:

                    color= tuple(img[0][ii])
                    r,g,b =  color
                    save_pixelF(r,g,b,dist12,2)
                    #print("Mb")
                    #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(ii)+"]")
                    dist12 = dist12 + 1
                    #print_msp()
                ii = ii + 1
            #matrix_2[aux_i][aux_j]=sum1
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
            
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
                #    print("Ma")
                   # print("f<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(x)+","+str(y)+"]")
                    save_pixelA(r,g,b,dist20,0,2,0,6)
                    dist20 = dist20 + 1
              #      print_msp()
                    #sum1+=matrix_1[x][y]
                   # print("==========="+str(sum1))
            #B
            xr=aux_j1
            dist22=1
            while xr<=rule_1:
                color= tuple(img[0][xr])
                r, g, b =  color
              #  print("Mb")
               # print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(xr)+"]")
                save_pixelG(r,g,b,dist22,2,0,6)
                dist22 = dist22 + 1
             #   print_msp()
                xr = xr + 1
            
            i5=aux_i1
            dist21=1
            #C
            while i5<=rule_1:
                color= tuple(img[i5][0])
                r, g, b =  color
                #print("Mc")
                #print("<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(i5)+","+str(0)+"]")
                save_pixelC(r,g,b,dist21,0,2,6,9)
                dist21 = dist21 + 1
                #print_msp()
                i5 = i5 + 1
                
         
            #D
            #print("Md") 
            color= tuple(img[0][0])
            r,g,b =  color
            save_pixelH(r,g,b,2,6,9)
           # print("f2<R "+str(r)+"> <G "+str(g)+"> <B "+str(b)+" > POINT ["+str(0)+","+str(0)+"]")
            #print_msp()
            npixel=operation()
            outputImg[aux_i][aux_j]=npixel[0]
            
            cv2.imwrite("/home/alien-ware/Documents/GitHub/Graphics/Processing Images/test_pics/newImage.png",outputImg)
        
        #clean values
        if sect_a==1 or sect_b==1 or sect_c==1 or sect_d==1 or sect_e==1 or sect_f==1 or sect_g==1 or sect_h==1 or sect_i==1:
            aux_j=0
            aux_i=0
            sum1=0
            npixel.clear()
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
                    matrix_saveOperation[clmx][clmy]=0
            
            #print("Data and matrix cleaned")


