rowIndex = 3

ret = []

for i in range(rowIndex+1):
    row = []
    for j in range(0, i+1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(ret[i-1][j] + ret[i-1][j-1])
    ret.append(row)

print(ret[rowIndex])