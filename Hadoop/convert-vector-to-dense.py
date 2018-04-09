
filename = 'File1ForLab3/outB3-final.list'
newfilename = 'File1ForLab3/newfiles/outB3.txt'
file = open(filename,'r')
newfile = open(newfilename,'w+')

size = file.readline().split()
rows = int(size[0])
cols = int(size [1])
newfile.write("%d %d \r\n" % ( rows,cols) )
rowCount = 0
colCount = 0
count = 0

with file:
    for line in file:
        value = line.split()
        x = int(value[0])
        y = int(value[1])



        if int(value[0]) == rowCount:
            newfile.write("%d %d %d\r\n" % (int(value[0]),int(value[1]),int(value[2])))
            rowCount +=1
        elif int(value[0]) > rowCount:
            while rowCount < x :
                newfile.write("%d %d %d\r\n" % (rowCount,0,0))
                rowCount += 1
            newfile.write("%d %d %d\r\n" % (int(value[0]), int(value[1]), int(value[2])))
            rowCount +=1








file.close()
newfile.close()