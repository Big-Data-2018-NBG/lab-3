from mrjob.job import MRJob
from mrjob.step import MRStep

import re
import os

WORD_RE = re.compile(r"[\w']+")


class MRMatrixReduce(MRJob):


    def steps(self):
        return [MRStep(mapper=self.mapper_one,
                       reducer=self.reducer_one),
                MRStep(mapper=self.mapper_two,
                       reducer=self.reducer_two)]

    def mapper_one(self, _, line):

        i,j,val = line.split()
        filename = os.environ['map_input_file']


        if filename == 'matrix1.txt':
            yield j, ('A', i, val)


        if filename =='matrix2.txt':
            yield i,('B',j,val)



    def reducer_one(self, j, values):
        list1 = []
        list2 = []

        for val in values:
            if val[0] == 'A':
                list1.append(val)
            if val[0] =='B':
                list2.append(val)

        for(a,i,val1) in list1:
            for(b,k,val2) in list2:
                yield (i,k),int(val1)*int(val2)


    def mapper_two(self, j, value):
        yield (j),value

    def reducer_two(self, key, value):
        yield key, sum(value)



    # def combiner(self, word, counts):
    #     yield (word, sum(counts))
    #
    # def reducer(self, word, counts):
    #     yield (word, sum(counts))



if __name__ == '__main__':

    MRMatrixReduce.run()



# https://github.com/uchicago-cs/cmsc12300/blob/master/examples/data_analysis/src/cs123/mrjob/matrixmult_2pass.py