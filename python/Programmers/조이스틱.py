def left(name, idx):
    i = (idx - 1) % len(name)
    cnt = 1
    while i != idx:
        if name[i] == "A":
            cnt += 1
        else:
            return [i, cnt]
        i = (i - 1) % len(name)
    else:
        return None

def right(name, idx):
    i = (idx + 1) % len(name)
    cnt = 1
    while i != idx:
        if name[i] == "A":
            cnt += 1
        else:
            return [i, cnt]
        i = (i + 1) % len(name)
    else:
        return None

def solution(name):
    res = 0
    tmp = [0] * 26
    for i in range(len(tmp)-1):
        if i >= 13:
            tmp[i+1] = tmp[i] - 1
        else:
            tmp[i+1] = tmp[i] + 1
    
    name = list(name)
    i = 0
    while True:
        res += tmp[ord(name[i]) - 65 ]
        name[i] = "A"
        l = left(name, i)
        r = right(name, i)

        if not l:
            return res

        if l[1] < r[1]:
            res += l[1]
            i = l[0]
        else:
            res += r[1]
            i = r[0]


print(solution("JEROEN"	))