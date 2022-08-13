nums = [1,1,0,1,1,1]

count = 0
n = len(nums)
ones = []
for fast in range(n):
    if nums[fast] == 1:
        count += 1
    elif nums[fast] != 1:
        ones.append(count)
        count = 0
    if fast == n - 1:
        ones.append(count)

max = ones[0]
for i in range(1, len(ones)):
    if ones[i] > max:
        max = ones[i]
