import random
from numpy import *
rows = 3
cols = 3

file = open('test.txt', 'w+')
file.write("%d %d\r\n" % (rows, cols))


def generatematrix(rows, cols):
    i = 0
    for x in range(rows):
        for y in range(cols):
            file.write("%d %d %d\r\n" % (x, y, i))
            # i = random.randint(0,5)
            i +=1

def transposeMatrix(m):
    for row in m:
        print(row)
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print("\n")
    for row in rez:
        print(row)


# m = range(3*2)
#
# m = reshape(m,(3,2))
#
#
# print(m)
#
#
# transposeMatrix(m)


generatematrix(rows, cols)
file.close()
