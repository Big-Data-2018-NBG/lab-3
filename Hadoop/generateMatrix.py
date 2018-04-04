import random

rows = 5
cols = 8

file = open('matrix2.txt', 'w+')
file.write("%d %d\r\n" % (rows, cols))


def generatematrix(rows, cols):
    i = 0
    for x in range(rows):
        for y in range(cols):
            file.write("%d %d %d\r\n" % (x, y, i))
            # i = random.randint(0,100)
            i +=1

generatematrix(rows, cols)
file.close()
