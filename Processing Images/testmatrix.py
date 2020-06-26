ns=9
ns1=3
matrix_savePixel= [[0] * ns for i in range(ns1)]
matrix_saveOperation=[[0] * ns for i in range(ns1)]
def print_mc():
    print("matrix savepixel")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

for xrt in range(0,2):
    for yrt in range(3,9):
        matrix_savePixel[xrt][yrt]=1
print_mc()

for xrt in range(3,9):
    matrix_savePixel[2][xrt]=2
print_mc()

for xrt in range(0,2):
    for yrt in range(0,3):
        matrix_savePixel[xrt][yrt]=3
print_mc()
for xrt in range(0,3):
    matrix_savePixel[2][xrt]=4
print_mc()