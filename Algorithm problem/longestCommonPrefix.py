
strs = ["flower","flow","flight"]
# 横向遍历法
def longestCommonPrefix1(strs):
    if not strs:
        return ''
    prefix, count = strs[0], len(strs)
    for i in range(1,count):
        prefix = lcp(prefix, strs[i])
        if not prefix:
            break

    return prefix


def lcp(str1, str2):
    length = min(len(str1), len(str2))
    index = 0
    while index < length and str1[index] == str2[index]:
        index += 1
    return str2[:index]


# 纵向遍历法
def longestCommonPrefix2(strs):
    if not strs:
        return ''
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != c or i == len(strs[j]):
                return strs[0][:i]

print(longestCommonPrefix2(strs))


# 分治法



# 二分查找法