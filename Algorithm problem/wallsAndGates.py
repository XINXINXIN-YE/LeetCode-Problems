
rooms =[
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
    ]

if not rooms or not rooms[0]: 
    print(None)

m, n = len(rooms), len(rooms[0])

queue = []
for r in range(m):
    for c in range(n):
        if rooms[r][c] == 0:
            queue.append((r,c))
dirs = [
    lambda x,y: (x+1, y),
    lambda x,y: (x-1, y),
    lambda x,y: (x, y+1),
    lambda x,y: (x, y-1)
]

while len(queue) > 0:
    r, c = queue.pop(0)
    for dir in dirs:
        nr, nc = dir(r,c)
        if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647:
            rooms[nr][nc] = rooms[r][c] + 1
            queue.append((nr, nc))
        
print(rooms)