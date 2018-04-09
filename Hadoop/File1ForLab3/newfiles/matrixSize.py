
def getDimenstions(name):
    file = open(name, 'r')
    size = file.readline().split()
    rows = size[0]
    cols = size[1]
    file.close()
    print(rows,cols)
    return (rows, cols)

