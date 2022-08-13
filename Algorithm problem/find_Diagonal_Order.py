import numpy as np
mat = [[1,2,3],[ 4,5,6],[7,8,9]]
mat  = np.array(mat)
m = len(mat)
n = len(mat[0])
print(m,n)
print('oringnal'+'\n')
print(mat)
out = []

for sum in range(m + n - 1):
    if sum % 2 == 0:
        for i in range(sum + 1):
            if i >= n or sum-i >= m:
                continue
            out.append(mat[sum - i][i])
    else:
        for i in range(sum + 1):
            if i >= m or sum-i >= n:
                continue
            out.append(mat[i][sum - i])

print(out)


'''
# 优化 速度比上面算法快99%
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        m = len(mat) #行数
        n = len(mat[0]) #列数
        tot = m + n - 1 #对角线条数
        res = []
        r, c = 0, 0  # r为横坐标，c为纵坐标，初始值都为零
        for i in range(tot):
            if i % 2 == 0:
                while r >= 0 and c < n: 
                    res.append(mat[r][c])
                    r -= 1 #横坐标向上移动一格
                    c += 1 #纵坐标向右移动一格
                if c < n:
                    r += 1
                else:
                    r += 2
                    c -= 1
            else:
                while c >= 0 and r < m: 
                    res.append(mat[r][c])
                    r += 1
                    c -= 1
                if r < m:
                    c += 1
                else:
                    c += 2
                    r -= 1
        return res
'''