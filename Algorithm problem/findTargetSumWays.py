
""" nums = [1,1,1,1,1]
target = 3
sum = sum(nums)
sumx = (target + sum) / 2

if target > sum or (target+sum) % 2 != 0:
    print(0)
for i in range(4,0,-1):
    print(i)

for i in range(0,4,-1):
    print(i)
 """
nums = [1,1,1,1,1]
target = 3

dp = {}

def backtrack(i,total):
    if i == len(nums):
        if total == target:
            return 1
        else:
            return 0
    if (i,total) in dp:
        return dp[(i,total)]

    dp[(i,total)] = (backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i]))
    return dp[(i,total)]

print(backtrack(0,0))
