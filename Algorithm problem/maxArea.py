
height = [1,8,6,2,5,4,8,3,7]
n = len(height)
areas = []
l = 0
r = n-1
maxarea = 0
while l < r:
    maxarea = max(maxarea,min(height[l], height[r])*(r-l))
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(maxarea)





















""" # 超时
height = [1,8,6,2,5,4,8,3,7]
n = len(height)
areas = []
for i in range(n):
    for j in range(i+1, n):
        h = min(height[i], height[j])
        l = j - i
        areas.append(h*l)
print(max(areas)) """