def solution(s):
    res = []
    tmp = s[2:-2].split("},{")
    tmp.sort(key= lambda x : len(x))
    for s in tmp:
        s = list(map(int, s.split(",")))
        res.append(list(set(s) - set(res))[0])
    return res

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))