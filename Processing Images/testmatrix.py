ns = 9
ns1 = 3
matrix_savePixel =  [[0] * ns for i in range(ns1)]
matrix_saveOperation = [[0] * ns for i in range(ns1)]
n=3
matrix_convolution = [[0] * n for i in range(n)]
matrix_pre = [[0] * n for i in range(n)]#save fraction

def print_mc():
    print(" [matrix savepixel]")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    print("\n")
def print_mc():
    print(" [matrix saveOperation]")
    for row in matrix_savePixel:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

def print_cm():
    print("[matrix_convolution]")
    for row in matrix_convolution:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

def print_mk():
    print(" [matrix_pre]")
    for row in matrix_pre:
        print(' '.join([str(elem) for elem in row]))
    print("\n")

"""
for x in range(0,2):
    for y in range(0,6):
        matrix_savePixel[x][y] = 1
print_mc()
for x in range(0,2):
    for y in range(6,9):
        matrix_savePixel[x][y] = 2
print_mc()
for y in range(6):
    matrix_savePixel[2][y] = 3
print_mc()
for y in range(6,9):
    matrix_savePixel[2][y] = 4
print_mc()

def operation():
    listnewpixel = []
    sector = 1
    for li in range(3):
        for lo in range(9):
            if sector == 1:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][0])
            if sector == 2:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][0])
            if sector == 3:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][0])
            if sector == 4:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][1])
            if sector == 5:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][1])
            if sector == 6:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][1])
            if sector == 7:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][2])
            if sector == 8:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][2])
            if sector == 9:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[0][2])
            if sector == 10:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][0])
            if sector == 11:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][0])
            if sector == 12:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][0])
            if sector == 13:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][1])
            if sector == 14:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][1])
            if sector == 15:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][1])
            if sector == 16:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][2])
            if sector == 17:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][2])
            if sector == 18:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[1][2])
            if sector == 19:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][0])
            if sector == 20:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][0])
            if sector == 21:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][0])
            if sector == 22:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][1])
            if sector == 23:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][1])
            if sector == 24:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][1])
            if sector == 25:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][2])
            if sector == 26:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][2])
            if sector == 27:
                matrix_saveOperation[li][lo] = int(matrix_savePixel[li][lo]*matrix_convolution[2][2])
"""