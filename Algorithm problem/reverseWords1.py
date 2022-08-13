
s = "hehhhhhhe"

l = 0
r = 0
res = []
ret = ''

while r < len(s):
    if s[r] != ' ':
        r += 1
        if r == len(s):
            if l != 0:
                res.append(s[r-1:l-1:-1])
            else:
                res.append(s[r-1::-1])
    elif s[r] == ' ':
        if l == 0:
            res.append(s[r-1::-1])
            r += 1
            l = r
            continue
        if l != 0:
            res.append(s[r-1:l-1:-1])
            r += 1
            l = r

ret = " ".join(res)
print(ret)

# 或者可以用逆向切片来完成
print(" ".join(word[::-1] for word in s.split(" ")))

# 还可以利用栈 先进后出的特性翻转字符串