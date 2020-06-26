ns=9
ns1=3
matrix_savePixel= [[0] * ns for i in range(ns1)]
matrix_saveOperation=[[0] * ns for i in range(ns1)]
def print_mc():
    print("matrix savepixel")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
"""
for xrt in range(1,3):
    for yrt in range(0,6):
        matrix_savePixel[xrt][yrt]=1
print_mc()

for xrt in range(6):
    matrix_savePixel[0][xrt]=2
print_mc()
"""
for xrt in range(0,3):
    for yrt in range(0,6):
        matrix_savePixel[xrt][yrt]=1
print_mc()
for xrt in range(0,3):
    for yrt in range(6,9):
        matrix_savePixel[xrt][yrt]=2
print_mc()