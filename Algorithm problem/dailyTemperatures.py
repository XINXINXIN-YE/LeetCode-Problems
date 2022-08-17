""" # 超时
temperatures = [55,38,53,81,61,93,97,32,43,78]
count = 1
slow = 0
output = []
while slow < len(temperatures):
    for fast in range(slow+1, len(temperatures)):
        if temperatures[slow] < temperatures[fast]:
            output.append(count)
            count = 1
            break
        else:
            count += 1
    else:
        output.append(0)
        count = 1
    slow += 1

print(output) """

# 单调栈
T = [73,74,75,71,69,72,76,73]
stack = []
res = [0] * len(T)

for i, t in enumerate(T):
    while stack and t > T[stack[-1]]:
        res[stack.pop()] = i - stack[-1]
    stack.append(i)

print(res)
