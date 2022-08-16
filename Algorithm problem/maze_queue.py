
# 经典迷宫算法：使用队列和广度优先搜索
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]

dirs = [
    lambda x,y: (x-1, y),#up
    lambda x,y: (x, y+1),#right
    lambda x,y: (x+1, y),#down
    lambda x,y: (x, y-1) #left
]

def print_r(path):
    curNode = path[-1]
    real_path = []

    while curNode[2] != -1:
        real_path.append(curNode[0:2])
        curNode = path[curNode[2]]
    real_path.append(curNode[0:2])
    real_path.reverse()
    print("path is:","\n",real_path)


def maze_path(x1,y1,x2,y2):
    queue = []
    queue.append((x1,y1,-1))
    path = []
    while len(queue) > 0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.insert(0, (nextNode[0], nextNode[1], len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2 # 标记为走过的
    else:
        print("no path")
        return False

maze_path(1,1,8,8)