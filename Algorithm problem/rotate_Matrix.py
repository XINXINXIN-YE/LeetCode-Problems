
import numpy as np
b = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
b  = np.array(b)
n = len(b)
print(b)
print('\n')

def clockwise_rot(b,n):
    '''顺时针旋转'''
    for i in range(n):
        for j in range(i):
            temp = b[i][j]
            b[i][j] = b[j][i]
            b[j][i] = temp

    for i in range(n):
        for j in range(n//2):
            temp1 = b[i][j]
            b[i][j] = b[i][-1-j]
            b[i][-1-j] = temp1
    
    print('clockwise_rot:'+'\n')
    print(b,'\n')

def anti_clockwise_rot(b,n):
    '''逆时针旋转矩'''
    for i in range(n):
        for j in range(i):
            temp = b[i][j]
            b[i][j] = b[j][i]
            b[j][i] = temp

    for i in range(n):
        for j in range(n//2):
            temp2 = b[j][i]
            b[j][i] = b[-1-j][i]
            b[-1-j][i] = temp2
    print('anti_clockwise_rot:'+'\n')
    print(b,'\n')

if __name__ == '__main__':

    anti_clockwise_rot(b,n)