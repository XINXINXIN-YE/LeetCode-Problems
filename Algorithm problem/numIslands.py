
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


m, n = len(grid), len(grid[0])
count = 0

dirs = [
    lambda x,y: (x-1, y),#up
    lambda x,y: (x, y+1),#right
    lambda x,y: (x+1, y),#down
    lambda x,y: (x, y-1) #left
]

def dfs(r,c):
    stack = []
    stack.append((r,c))
    while len(stack) > 0:
        r,c = stack[-1]
        for dir in dirs:
            nr, nc = dir(r,c)
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                stack.append((nr,nc))
                grid[nr][nc] = '0'
                break
        else:
            grid[r][c] = '0'
            stack.pop()
    else:
        return None

for r in range(m):
    for c in range(n):
        if grid[r][c] == '1':
            count += 1
            grid[r][c] = '0'
            dfs(r, c)
print(count)



