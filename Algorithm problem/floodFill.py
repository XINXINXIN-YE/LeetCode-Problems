
image = [
    [0,0,0],
    [0,0,0]
]

sr,sc = 0, 0
color = 0
m = len(image)
n = len(image[0])

dirs = [
    lambda x,y: (x-1,y),
    lambda x,y: (x+1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1)
]
def floodfill(sr,sc):
    if color == image[sr][sc]:
        return image
    else:
        queue = []
        queue.append((sr,sc))
        initial = image[sr][sc]
        image[sr][sc] = color
        while queue:
            sr,sc = queue.pop()
            for dir in dirs:
                nr,nc = dir(sr,sc)
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == initial:
                    queue.append((nr,nc))
                    image[nr][nc] = color
        return image

print(floodfill(sr,sc))

