nums = [0,0,1]

# 冒泡交换非零元素
""" l = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[l] = nums[l], nums[i]
        l += 1
    
print(nums) """

# 移除0再添加0
slow = 0
count = 0

for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow] = nums[fast]
        slow += 1
    else:
        count += 1
print(count)
print(nums)
for i in range(1,count+1):
    nums[-i] = 0

print(nums)