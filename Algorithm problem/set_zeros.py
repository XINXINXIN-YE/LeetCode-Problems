import numpy as np
from numpy import piecewise
b = [[ 0, 1, 2, 0],[ 3, 4, 5, 2],[1, 3, 1, 5]]
b  = np.array(b)
n = len(b)
m = len(b[0])
print('oringnal'+'\n')
print(b)
row = []
column = []
# 检查行有无零元素
for i in range(n):
    for j in range(m):
        if b[i][j] == 0:
            row.append(i)

# 检查列有无零元素
for i in range(n):
    for j in range(m):
        if b[i][j] == 0:
            column.append(j)

row = list(set(row))
cloumn = list(set(column))

l = len(row)
l1 = len(column)
# row = 0
for i in range(l):
    for j in range(m):
        b[row[i]][j] = 0

# column = 0
for i in range(l1):
    for j in range(n):
        b[j][column[i]] = 0

print('set_zeros'+'\n')
print(b)

