
s = "100[leetcode]"

stack = []
res = ''
mul = 0

for item in s:
    if '0' <= item <= '9':
        mul = mul * 10 + int(item)
    elif item == '[':
        stack.append((mul,res))
        mul = 0
        res = ''
    elif item == ']':
        cur_mul, last_res = stack.pop()
        res = last_res + cur_mul * res
    else:
        res += item
print(res)