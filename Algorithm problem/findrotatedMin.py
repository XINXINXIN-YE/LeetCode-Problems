
""" nums = [1]
num_new = nums.copy()

if len(nums) == 1:
    print(nums[0])
while 1:
    if num_new[0] < nums[-1]:
        break
    for i in range(len(nums)):
        num_new[i] = nums[i-1]
    nums = num_new.copy()
    
print(nums[0]) """

nums = [1,1,2]
nums = list(set(nums))
print(nums)