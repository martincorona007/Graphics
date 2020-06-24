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
control=1
for ixt in range(1,3):
    for iyt in range(3,9):
        #print(" ixt "+str(ixt)+" iyt "+str(iyt))
        if 1==control:
            #print("s1")
            matrix_savePixel[ixt][iyt]=1
        if 2==control:
            #print("s2")
            matrix_savePixel[ixt][iyt]=2
        if 3==control:
            #print("s3")
            matrix_savePixel[ixt][iyt]=3
        if 4==control:
            #print("s1")
            matrix_savePixel[ixt][iyt]=1
        if 5==control:
            #print("s2")
            matrix_savePixel[ixt][iyt]=2
        if 6==control:
            #print("s3")
            matrix_savePixel[ixt][iyt]=3
        if 7==control:
            #print("s1")
            matrix_savePixel[ixt][iyt]=1
        if 8==control:
            #print("s2")
            matrix_savePixel[ixt][iyt]=2
        if 9==control:
            #print("s3")
            matrix_savePixel[ixt][iyt]=3
        if 10==control:
            #print("s1")
            matrix_savePixel[ixt][iyt]=1
        if 11==control:
            #print("s2")
            matrix_savePixel[ixt][iyt]=2
        if 12==control:
            #print("s3")
            matrix_savePixel[ixt][iyt]=3
        control = control + 1    
        #matrix_savePixel[ixt][iyt]=1

#print_mc()

for ixt1 in range(3,9):
    if 13==control:
            #print("s1")
        matrix_savePixel[0][ixt1]=1
    if 14==control:
            #print("s2")
        matrix_savePixel[0][ixt1]=2
    if 15==control:
            #print("s3")
        matrix_savePixel[0][ixt1]=3
    if 16==control:
            #print("s1")
        matrix_savePixel[0][ixt1]=1
    if 17==control:
            #print("s2")
        matrix_savePixel[0][ixt1]=2
    if 18==control:
            #print("s3")
        matrix_savePixel[0][ixt1]=3
    control = control + 1  
    #matrix_savePixel[0][ixt1]=2
#print_mc()
for ixt2 in range(1,3):
    for iyt2 in range(0,3):
        if 19==control:
            #print("s1")
            matrix_savePixel[ixt2][iyt2]=1
        if 20==control:
                #print("s2")
            matrix_savePixel[ixt2][iyt2]=2
        if 21==control:
                #print("s3")
            matrix_savePixel[ixt2][iyt2]=3
        if 22==control:
                #print("s1")
            matrix_savePixel[ixt2][iyt2]=1
        if 23==control:
                #print("s2")
            matrix_savePixel[ixt2][iyt2]=2
        if 24==control:
                #print("s3")
            matrix_savePixel[ixt2][iyt2]=3
        control = control + 1   
        #print(" ixt "+str(ixt2)+" iyt "+str(iyt2))
         #matrix_savePixel[ixt2][iyt2]=3
#print_mc()
for ixt3 in range(0,3):
     if 25==control:
                #print("s1")
        matrix_savePixel[0][ixt3]=1
     if 26==control:
                #print("s2")
        matrix_savePixel[0][ixt3]=2
     if 27==control:
                #print("s3")
        matrix_savePixel[0][ixt3]=3
     control = control + 1 
    #matrix_savePixel[0][ixt3]=4
print_mc()
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
        
        print(" itli "+str(itli)+" itlo "+str(itlo))
print_so()
for clx in range(3):
    for cly in range(9):
        if matrix_saveOperation[clx][cly]<0:
            matrix_saveOperation[clx][cly]=matrix_saveOperation[clx][cly]*-1
print_so()