def DFS(L, tmp):
    if L == len(nums):
        res.append(tmp[:])
    else:
        DFS(L+1, tmp)
        DFS(L+1, tmp+[nums[L]])

nums = [1,2,3]
res = []
DFS(0, [])
print(res)