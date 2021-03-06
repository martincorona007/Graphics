def print_mc():
    print("Convolution Mask")
    for row in matrix_convolution:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

def print_mk():
    
    for row in matrix_pre:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
def print_so():
    for row in matrix_saveOperation:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

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
anws=int(input("Do you want bias? yes=1 no=0 "))
if anws==1:
    bias=1
    anwsr=int(input("Number bias: "))
    biasv=anwsr
else:
    bias=0
"""
The [matrix_pre] is to get a float number and multiple it by the original convolution mask[matrix_convolution].
"""
for i in range(n):
    for j in range(n):
        matrix_pre[i][j]=lc

print_mk()
print("Convolution: ")
for i in range(n):
    for j in range(n):
        matrix_convolution[i][j]=int(input("Enter number: "))
        print_mc()
for i in range(n):
    for j in range(n):
        matrix_convolution[i][j]=matrix_pre[i][j]*(matrix_convolution[i][j])

print_mc()

ns=9
ns1=3
matrix_savePixel= [[0] * ns for i in range(ns1)]
matrix_saveOperation=[[0] * ns for i in range(ns1)]
def print_mc():
    print("matrix savepixel")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    print("\n")


#print_mc()
def operation():
    listnewpixel=[]
    sector=1
    for itli in range(3):
        for itlo in range(9):
            if sector==1:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][0])
            if sector==2:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][0])
            if sector==3:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][0])
            if sector==4:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][1])
            if sector==5:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][1])
            if sector==6:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][1])
            if sector==7:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][2])
            if sector==8:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][2])
            if sector==9:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[0][2])
            if sector==10:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][0])
            if sector==11:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][0])
            if sector==12:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][0])
            if sector==13:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][1])
            if sector==14:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][1])
            if sector==15:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][1])
            if sector==16:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][2])
            if sector==17:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][2])
            if sector==18:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[1][2])
            if sector==19:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][0])
            if sector==20:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][0])
            if sector==21:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][0])
            if sector==22:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][1])
            if sector==23:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][1])
            if sector==24:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][1])
            if sector==25:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][2])
            if sector==26:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][2])
            if sector==27:
                matrix_saveOperation[itli][itlo]=int(matrix_savePixel[itli][itlo]*matrix_convolution[2][2])
            
            sector = sector + 1
            
            #print(" itli "+str(itli)+" itlo "+str(itlo))
    print_so()
    #remove negative numbers
    for clx in range(3):
        for cly in range(9):
            if matrix_saveOperation[clx][cly]<0:
                matrix_saveOperation[clx][cly]=matrix_saveOperation[clx][cly]*-1
    print_so()
    R=0
    G=0
    B=0
    for oxl in range(3):
        R+=matrix_saveOperation[oxl][0]+matrix_saveOperation[oxl][3]+matrix_saveOperation[oxl][6]
        G+=matrix_saveOperation[oxl][1]+matrix_saveOperation[oxl][4]+matrix_saveOperation[oxl][7]
        B+=matrix_saveOperation[oxl][2]+matrix_saveOperation[oxl][5]+matrix_saveOperation[oxl][8]
    if bias==1:
        print("with bias")
        if R>=biasv:
            R=biasv
        if G>=biasv:
            G=biasv
        if B>=biasv:
            B=biasv
    else:
        print("without bias")
        if R>=255:
            R=255
        if G>=255:
            G=255
        if B>=255:
            B=255
        if R<0:
            R=0
        if G<0:
            G=0
        if B<0:
            B=0
             #print("1p R "+str(R)+" G "+str(G)+" B "+str(B))
    print("2p R "+str(R)+" G "+str(G)+" B "+str(B))
    saveNP=[R,G,B]
    listnewpixel.append(saveNP)
    return listnewpixel
   