from matplotlib import pyplot as plt
#==============MATRIX A ==============
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
print("Traslation")
#==============MATRIX B==============
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
#==============ASK DATA============== 
#Px=4
#Py=1
print("Enter Point")
Px=int(input("Enter Px number: "))
Py=int(input("Enter Py number: "))
b[0][0]=Px
b[1][0]=Py   

tx=int(input("Enter tx number: "))
ty=int(input("Enter ty number: "))

#tx=-2
#ty=2
a[0][2]=tx
a[1][2]=ty
#==============PRINT==============
print("Matrix A")
for row in a:
    print(' '.join([str(elem) for elem in row]))
print("Matrix B")
for row in b:
    print(row);

#==============MATRIX RESULT==============
c1=m2
r1=n1
result_array=[ [0] * c1 for i in range(r1)]

#==============OPERATION==============
for i in range(n1):
    for j in range(m2):
        for x in range(n1):
            result_array[i][j]=a[i][x]*b[x][j]+result_array[i][j]

print("Result")
for row in result_array:
    print(row);

#==============Graph==============
plt.plot(Px,Py, marker="o", color="red")
plt.plot(result_array[0][0],result_array[1][0], marker="D", color="blue")
plt.title("Traslation")
plt.yticks([i for i in range(10)]) 
plt.xticks([i for i in range(10)]) 
plt.xlabel("X")
plt.ylabel("Y")
plt.show()