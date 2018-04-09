from matrixSize import getDimenstions
from mrjob.job import MRJob

import re
import os
import time

WORD_RE = re.compile(r"[\w']+")
matrixMDim = getDimenstions('outA1.list')
matrixNDim = getDimenstions('outB1.list')
i = int(matrixMDim[0])
j = int(matrixMDim[1])
k = int(matrixNDim[1])
print(j)
class MRMatrixReduce(MRJob):


    def mapper(self, _, line):

        x = line.split()
        if len(x) == 2:
            return

        row, col, value = line.split()
        matrixAList = []
        matrixBList = []
        filename = os.environ['map_input_file']
        value = int(value)
        row = int(row)
        col = int(col)
        # print(filename)
        if filename == 'outA1.list':
            matrixAList.append((row, col, value))
            for x in range(k):
                #print((row,x),('M',col,value))
                yield (row,x),('M',col,value)

        if filename == 'outB1.list':
            matrixBList.append((row, col, value))
            for x in range(i):
                #print((x,col),('N',row,value))
                yield (x,col),('N',row,value)


    def reducer(self, key, val):

        listM =[]
        listN =[]
        listAns=[]

        for values in val:
            if values[0] == 'M':
                listM.append((values[1],values[2]))
            elif values[0] == 'N':
                listN.append(values[2])

        print(len(listM))
        print(len(listN))
        for x in range(0,j):
           listAns.append(listM[x] * listN[x])

        yield key, sum(listAns)


if __name__ == '__main__':
    start = time.time()
    MRMatrixReduce.run()
    end = time.time()
    print(end-start)



