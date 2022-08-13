s = "A man, a plan, a canal: Panama"

if len(s) == 0:
    print('true')
s="".join(filter(str.isalnum, s))
s = s.lower()
print(s)
l = 0
r = len(s)-1
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        print('false')
        break

print('true')
