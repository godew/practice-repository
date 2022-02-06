def DFS(L,s):
    if sum(tmp) > target:
        return
    if sum(tmp) == target:
        res.append(tmp[:])
    else:
        for i in range(s, len(candidates)):
            tmp.append(candidates[i])
            DFS(L+1, i)
            tmp.pop()

    
candidates = [2,3,6,7]; target = 7
res = []
tmp = []
DFS(0,0)

print(res)


