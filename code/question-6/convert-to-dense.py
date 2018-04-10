
# filename = 'File1ForLab3/outA3.list'
# newfilename = 'File1ForLab3/newfiles/outA3.txt'
filename = 'outNetworkB.list'
newfilename = 'newNetwork.txt'

file = open(filename,'r')
newfile = open(newfilename,'w+')

size = file.readline().split()
rows = int(size[0])
cols = int(size [1])
newfile.write("%d %d \r\n" % ( rows,cols))
rowCount = 0
colCount = 0
count = 0

with file:
    for line in file:
        # print(line)
        value = line.split()
        x = int(value[0])
        # print(x)
        y = int(value[1])

        if colCount < cols and x > rowCount:

            while colCount < cols :
                newfile.write("%d %d %d\r\n" % (rowCount, colCount, 0))
                colCount += 1
        #
        # if colCount < cols and rowCount < rows:
        #
        #     while colCount < cols :
        #         newfile.write("%d %d %d\r\n" % (rowCount, colCount, 0))
        #         colCount += 1



        if int(value[1]) == colCount:
            newfile.write("%d %d %d\r\n" % (int(value[0]),int(value[1]),int(value[2])))
            # print("%d %d %d\r\n" % (int(value[0]),int(value[1]),int(value[2])))
            colCount +=1
        elif int(value[1]) > colCount:
            while colCount < y :
                newfile.write("%d %d %d\r\n" % (x,colCount,0))
                # print("%d %d %d\r\n" % (x,colCount,0))
                colCount += 1

            newfile.write("%d %d %d\r\n" % (int(value[0]), int(value[1]), int(value[2])))
            # print("%d %d %d\r\n" % (int(value[0]), int(value[1]), int(value[2])))
            colCount +=1


        if colCount == cols:
            colCount = 0
            rowCount +=1




file.close()
newfile.close()
