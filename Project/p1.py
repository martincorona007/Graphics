from matplotlib import pyplot as plt
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
print("Traslation")
#==============MATRIX B==============
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
#==============ASK DATA============== 
#Px=4
#Py=1
print("Enter Point")
Px=float(input("Enter Px number: "))
Py=float(input("Enter Py number: "))
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
#create the matrix result
c1=m2
r1=n1
result_array=[ [0] * c1 for i in range(r1)]

#==============OPERATION multiplication==============
for i in range(n1):
    for j in range(m2):
        for x in range(n1):
            result_array[i][j]=a[i][x]*b[x][j]+result_array[i][j]

print("Result")
for row in result_array:
    print(row);

#==============Graph==============
plt.plot(Px,Py, marker="o", color="red")#mark point px and py
plt.plot(result_array[0][0],result_array[1][0], marker="D", color="blue") #mark the result point
plt.title("Traslation")
plt.yticks([i for i in range(-20,21)]) #set size to the cartesian plan
plt.xticks([i for i in range(-20,21)]) #set size to the cartesian plan
plt.axhline(0, color='black') #draw color black in the cartesian plan
plt.axvline(0, color='black')#draw color black in the cartesian plan
plt.quiver(result_array[0][0],result_array[1][0], angles='xy', scale_units='xy', scale=1,color="blue")#draw a row
plt.xlabel("X")
plt.ylabel("Y")

plt.show()