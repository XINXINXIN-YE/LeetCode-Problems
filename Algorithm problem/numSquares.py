# BFS1
""" n = 12

queue = [n]
visited = set()
count  = 0

if n == 0:
    print(0)
while queue:
    count += 1
    l = len(queue)
    for _ in range(l):
        tmp = queue.pop()
        for i in range(1, int(tmp ** 0.5) + 1):
            x = tmp - i ** 2
            if x == 0:
                print(count)
                exit()
            if x not in visited:
                visited.add(x)
                queue.insert(0, x)
    
print(count) """
# BFS2
n = 12
squares = [i ** 2 for i in range(1, int(n ** .5) + 1)]
level = [n]
count = 0

while level:
    next_level = set()
    for rem in level:
        if rem == 0:
            print(count)
            exit()
        for square in squares:
            if rem < square:
                break
            next_level.add(rem - square)
    count += 1
    level = next_level
print(count)