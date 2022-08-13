
haystack = "aaaaa"
needle = 'bba'
m = len(haystack)
n = len(needle)

if not needle:
    print(0)

for i in range(m-n+1):
    if haystack[i] == needle[0]:
        if haystack[i:i+n] == needle:
            print(i)
print(-1)