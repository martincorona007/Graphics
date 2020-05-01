from matplotlib import pyplot as plt
import math
#==============MATRIX A 
#Create matrix A and initialate the matrix with 0 and 1
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
print("Hello Future")
#==============MATRIX B
#Create the matrix B and initialate the matrix with 1
n2 = r = 3
m2 = c = 1

b = [[0] * c for i in range(r)]
for i in range(r):
    for j in range(c):
        b[i][j] = 1
"""        
for row in b:
    print(row);
"""
#==============ASK DATA 
#Px=6
#Py=1
Px=int(input("Enter Px number: "))
Py=int(input("Enter Py number: "))
b[0][0]=Px
b[1][0]=Py   

#ro=45
ro=int(input("Enter Rotation: "))
a[0][0]=round(math.cos(math.radians(ro)),2)
a[0][1]=round(math.sin(math.radians(-ro)),2)
a[1][0]=round(math.sin(math.radians(ro)),2)
a[1][1]=round(math.cos(math.radians(ro)),2)
##NOTE
#When I use the function round, it only takes the two decimal numbers and add 1
#==============PRINT
print("Matrix A")
for row in a:
    print(' '.join([str(elem) for elem in row]))
print("Matrix B")
for row in b:
    print(row);
#===MATRIX RESULT
c1=m2
r1=n1
result_array=[ [0] * c1 for i in range(r1)]

#===OPERATION
for i in range(n1):
    for j in range(m2):
        for x in range(n1):
            result_array[i][j]=a[i][x]*b[x][j]+result_array[i][j]

print("Result")
for row in result_array:
    print(row);

#Graph
xx1=[0,Px]
yy1=[0,Py]
xx2=[0,result_array[0][0]]
yy2=[0,result_array[1][0]]
yy=[0,result_array[1][0]]

plt.plot(Px,Py, marker="o", color="red")
plt.plot(xx1,yy1, marker="+", color="red")
plt.plot(result_array[0][0],result_array[1][0], marker="D", color="blue")
plt.plot(xx2,yy2, marker="+", color="blue")

plt.title("Rotation")
plt.yticks([i for i in range(10)]) 
plt.xticks([i for i in range(10)]) 
plt.xlabel("X")
plt.ylabel("Y")
plt.show()