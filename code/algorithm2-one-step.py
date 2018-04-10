from mrjob.job import MRJob
from matrixSize import getDimenstions
import re
import os
import time

WORD_RE = re.compile(r"[\w']+")
matrixMDim = getDimenstions('outA3.list')
matrixNDim = getDimenstions('outB3-final.list')
i = int(matrixMDim[0])
j = int(matrixMDim[1])
k = int(matrixNDim[1])

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
        if filename == 'outA3.list':
            matrixAList.append((row, col, value))
            for x in range(k):
                # print((row,x),('M',col,value))
                yield (row,x),('M',col,value)

        if filename == 'outB3-final.list':
            matrixBList.append((row, col, value))
            for x in range(i):
                # print((x,col),('N',row,value))
                yield (x,col),('N',row,value)


    def reducer(self, key, val):

        listM =[0]*int(j)
        listN =[0]*int(j)
        listAns=[]

        for values in val:
            
            if values[0] == 'M':
                position = values[1]
                listM[position] = values[2]

            elif values[0] == 'N':
                position = values[1]
                listN[position] = values[2]

        for x in range(0,len(listM)):
 
           listAns.append(listM[x] * listN[x])

        yield key, sum(listAns)


if __name__ == '__main__':
    start = time.time()
    MRMatrixReduce.run()
    end = time.time()
    print(end-start)



