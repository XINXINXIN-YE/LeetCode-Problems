
s = 'the sky is blue'
s1 = ''


res = []

# 第一步先去除首尾的空格
def remove_outside_spaces(s):
    global s1
    l, r = 0, len(s) - 1
    while s[l] == ' ' :
        l += 1
        if s[l] != ' ':
            break

    while s[r] == ' ':
        r -= 1
        if s[r] != ' ':
            break
    s1 = s[l: r+1]
    return s1

# 从后往前挑单词
def select_words_from_back(s):
    right = len(s) - 1
    left = len(s) - 1

    while left >= 0:
        if s[left] != ' ':
            if left == 0:
                res.append(s[left: right+1])
            left -= 1
        if s[left] == ' ':
            res.append(s[left+1: right+1])
            while(1):
                left -= 1
                if s[left] != ' ':
                    right = left
                    break
    return res

# 把list的内容合起来
space = ' '

remove_outside_spaces(s)
select_words_from_back(s1)
print(space.join(res))



