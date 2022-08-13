
# 冒泡排序 可惜超时间
nums = [1,1,2,2,3]
sum = 0
x = 1
for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
while x < len(nums):
    sum += nums[x]
    x += 2
print(nums)
print(sum)