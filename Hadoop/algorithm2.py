from matrixSize import getDimenstions
from mrjob.job import MRJob
from mrjob.step import MRStep

import re
import os


WORD_RE = re.compile(r"[\w']+")
matrixMDim = getDimenstions('matrix1.txt')
matrixNDim = getDimenstions('matrix2.txt')
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
        if filename == 'matrix1.txt':
            matrixAList.append((row, col, value))
            for x in range(k):
                # print((row,x),('M',col,value))
                yield (row,x),('M',col,value)

        if filename == 'matrix2.txt':
            matrixBList.append((row, col, value))
            for x in range(i):
                # print((x,col),('N',row,value))
                yield (x,col),('N',row,value)


    def reducer(self, key, val):

        listM =[]
        listN =[]
        listAns=[]

        for values in val:
            if values[0] == 'M':
                listM.append(values[2])
            elif values[0] == 'N':
                listN.append(values[2])

        for x in range(0,j):
           listAns.append(listM[x] * listN[x])



        yield key, sum(listAns)





if __name__ == '__main__':

    MRMatrixReduce.run()



