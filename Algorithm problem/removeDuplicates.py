# 移除重复元素Ⅰ
""" nums = [1,1,1,2,2,3]

slow = 0
fast = 1

while slow < len(nums) and fast < len(nums):
    if nums[slow] == nums[fast]:
        fast += 1
    elif nums[slow] != nums[fast]:
        slow += 1
        nums[slow] = nums[fast]
print(nums) """


# 移除重复元素Ⅱ
nums = [0,0,1,1,1,1,2,3,3]

slow = 1

for fast in range(2, len(nums)):
    if nums[fast] == nums[slow] and nums[fast] == nums[slow - 1]:
        continue
    slow += 1
    nums[slow] = nums[fast]
print(nums)


