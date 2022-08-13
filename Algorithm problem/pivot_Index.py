'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''
# 致命缺点：遇到数组内含负数就不行了。
nums = [-1,-1,-1,-1,-1,0]
len = len(nums)
m = len//2


def left_sum():
    global m
    left = 0
    for i in range(m):
        left += nums[i]
    return left

def right_sum():
    global m
    right = 0
    for i in range(m + 1, len):
        right += nums[i]
    return right

def judge_and_move():
    global m
    while(1):
        if left_sum() > right_sum():
            m -= 1
            if m == 0:
                if left_sum() != right_sum():
                    return -1
                    break
        elif left_sum() < right_sum():
            m += 1
            if m == (len - 1):
                if left_sum() != right_sum():
                    return -1
                    break
        elif left_sum() == right_sum():
            return m
            break


print(judge_and_move())