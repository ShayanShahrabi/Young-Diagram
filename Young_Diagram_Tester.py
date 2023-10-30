import random
from Young_Diagram import *
#-----------------------------------------------------------------------------
# main program
n = int(input("Input the number of elements in your array: "))
array = []
for _ in range(n):
    array.append(random.randint(10, 99))
print("Created array:", array)
rowNum = int(input("Input the number of rows in your 2D matrix: ")) 
colNum = int(input("Input the number of columns in your 2D matrix: ")) 

Z = matrixMakerRowMaj(array, rowNum, colNum)

Z.printTable()

Z.buildYoungTable()

Z.printTable()
