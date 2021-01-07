ns=9
ns1=3
matrix_savePixel= [[0] * ns for i in range(ns1)]
matrix_saveOperation=[[0] * ns for i in range(ns1)]
def print_mc():
    print("matrix savepixel")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

for x in range(0,2):
    for y in range(0,6):
        matrix_savePixel[x][y]=1
print_mc()
for x in range(0,2):
    for y in range(6,9):
        matrix_savePixel[x][y]=2
print_mc()
for y in range(6):
    matrix_savePixel[2][y]=3
print_mc()
for y in range(6,9):
    matrix_savePixel[2][y]=4
print_mc()