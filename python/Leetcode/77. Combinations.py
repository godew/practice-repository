# def DFS(L, s):
#     if L == k:
#         res.append(tmp[:])
#     else:
#         for i in range(s, n+1):
#             tmp.append(i)
#             DFS(L+1, i+1)
#             tmp.pop()

# n = 4; k = 2
# res = []
# tmp = []
# DFS(0,1)

# print(res)

import itertools
n = 4; k = 2
print(list(map(list, itertools.combinations(range(1,n+1), k))))