# This script will find the total number of paths in a final matrix.

file = open('matrix-cubed.txt', 'r')
sum =0;
with file:
    for line in file:
        x,y,val = line.split()
        val = int(val)
        x = int(x)
        y = int(y)
        if x != y:
            sum += val

print(sum)
file.close()
