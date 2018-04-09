filename = 'File1ForLab3/outB3.list'
newfilename = 'File1ForLab3/outB3-final.list'
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
    for value in file:
        line = value.split()
        newfile.write('%d %d %d\r\n' % (int(line[0]), 0, int(line[1])))