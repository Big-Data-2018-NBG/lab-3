import random
from numpy import *
import time


num = 150
x = range(num*num)

x = reshape(x,(num,num))
# print(x)

y = range(num*num)
y = reshape(y,(num,num))

# print(y)
rowsX = len(x)
colsX = len(x[0])
rowsY = len(y)
colsY = len(y[0])


C = [[0 for row in range(len(x))] for col in range(len(x[0]))]
# print(C)


start = time.time()
for i in range(rowsX):
    for j in range(colsY):
        for k in range(colsX):
            C[i][j] += x[i][k] * y[k][j]
# print("\r\n")
end = time.time()
print(end- start)
# print(C)