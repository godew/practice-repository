s = "a"

MAX = -1
for idx in range(len(s)):
    for i in range(1, len(s)+1):
        if 0 > idx-i or idx+i >= len(s) or s[idx-i] != s[idx+i]:
            if MAX < i:
                MAX = i
                res = s[idx-i+1:idx+i]
            break

    if idx+1 != len(s) and s[idx] == s[idx+1]:
        for i in range(1, len(s)):
            if 0 > idx-i or idx+1+i >= len(s) or s[idx-i] != s[idx+1+i]:
                if MAX <= i:
                    MAX = i
                    res = s[idx-i+1:idx+1+i]
                break

print(res)

