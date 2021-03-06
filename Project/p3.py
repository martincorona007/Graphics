from matplotlib import pyplot as plt
import math
#==============MATRIX A ==============
#Create matrix A and initialate the matrix with 0 and 1, n1 & n is the  rows
n1 = n = 3
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 0
        else:
            a[i][j] = 1
"""
for row in a:
    print(' '.join([str(elem) for elem in row]))
"""

#==============MATRIX B ==============
#Create the matrix B and initialate the matrix with 1
n2 = r = 3#rows
m2 = c = 1#columns

b = [[0] * c for i in range(r)]
for i in range(r):
    for j in range(c):
        b[i][j] = 1
"""        
for row in b:
    print(row);
"""
#==============MATRIX C ==============
#Create matrix A and initialate the matrix with 0 and 1, n3 & n4 is the  rows
n3 = n4 = 3
c = [[0] * n4 for i in range(n4)]
for i in range(n4):
    for j in range(n4):
        if i < j:
            c[i][j] = 0
        elif i > j:
            c[i][j] = 0
        else:
            c[i][j] = 1
"""
for row in a:
    print(' '.join([str(elem) for elem in row]))
"""

#==============MATRIX D==============
#Create the matrix B and initialate the matrix with 1
n3 = r1 = 3#rows
m3 = c1 = 1#columns

d = [[0] * c1 for i in range(r1)]
for i in range(r1):
    for j in range(c1):
        d[i][j] = 1
"""        
for row in b:
    print(row);
"""
#==============ASK DATA ==============
print("Escalation")
print("Insert Point 1 P1")
Px1=float(input("Enter Px number: "))
Py1=float(input("Enter Py number: "))

print("Insert Point 2 P2")
Px2=float(input("Enter Px number: "))
Py2=float(input("Enter Py number: "))

print("Insert Values Sx and Sy")
k=Sx=float(input("Enter Sx number: "))
k1=Sy=float(input("Enter Sy number: "))
"""
Px1=1
Py1=1

Px2=3
Py2=2

Sx=2
Sy=3
"""


a[0][0]=Sx
a[1][1]=Sy

b[0][0]=Px1
b[1][0]=Py1

c[0][0]=Sx
c[1][1]=Sy

d[0][0]=Px2
d[1][0]=Py2


#==============MATRIX RESULT 1==============
#create the matrix result
c1=m2
r1=n1
result_array=[ [0] * c1 for i in range(r1)]

#==============MATRIX RESULT 2==============
#create the matrix result
cc1=m3
rr1=n3
result_array1=[ [0] * cc1 for i in range(rr1)]

#==============OPERATION==============
for i in range(n1):
    for j in range(m2):
        for x in range(n1):
            result_array[i][j]=a[i][x]*b[x][j]+result_array[i][j]

for i in range(n3):
    for j in range(m3):
        for x in range(n3):
            result_array1[i][j]=c[i][x]*d[x][j]+result_array1[i][j]



#==============PRINT==============
print("Matrix A")
for row in a:
    print(' '.join([str(elem) for elem in row]))
print("Matrix B")
for row in b:
    print(row);
print("Result 1")
for row in result_array:
    print(row);
print("++++++++++")
print("Matrix C")
for row in c:
    print(' '.join([str(elem) for elem in row]))
print("Matrix D")
for row in d:
    print(row);
print("Result 2")
for row in result_array1:
    print(row);

#=============Graph==============
#mark points and lines
xx1=[Px1,Px2]#Point 1 px py
yy1=[Py1,Py2]#Point 2 px py

xx2=[result_array[0][0],result_array1[0][0]]#result matrix
yy2=[result_array[1][0],result_array1[1][0]]#result matrix
plt.plot(xx1,yy1, marker="o", color="red")#graph the point px and py 
plt.plot(xx2,yy2, marker="o", color="blue")#graph the point 'px and 'py
plt.title("Escalation")
plt.yticks([i for i in range(-15,16)]) #set size to the cartesian plan
plt.xticks([i for i in range(-15,16)])#set size to the cartesian plan
plt.axhline(0, color='black')
plt.axvline(0, color='black') 
plt.xlabel("X")
plt.ylabel("Y")
plt.show()