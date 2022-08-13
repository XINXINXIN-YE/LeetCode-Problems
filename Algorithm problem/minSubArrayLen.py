nums = [2,3,1,2,4,3]
target = 7

# 双指针：尺取法
left, right = 0, 0
sum = 0
count = len(nums) + 1 # 全部加起来刚好是target和仍然不满足target的分界
for right in range(len(nums)):
    sum += nums[right]
    while sum >= target:
        count = min(right - left + 1, count)
        sum -= nums[left]
        left += 1
if count == len(nums) + 1:
    print(0)
else:
    print(count)


# 很遗憾 这个方法超时AC不了
'''
sum = 0
arry = []
for slow in range(len(nums)):
    fast = slow
    sum = 0
    while fast < (len(nums)):
        sum += nums[fast]
        if sum >= target:
            sum = 0
            arry.append(fast - slow + 1)
            break
        fast += 1
if not arry:
    print(0)
else:
    print(min(arry))
'''







