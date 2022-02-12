# def DFS(L):
#     if L == len(nums):
#         res.append(tmp[:])
#     else:
#         for i in range(len(nums)):
#             if ch[i] == 0:
#                 tmp[L] = nums[i]
#                 ch[i] = 1
#                 DFS(L+1)
#                 ch[i] = 0

# nums = [1,2,3]
# tmp = [0]*len(nums)
# ch = [0]*len(nums)
# res = []
# DFS(0)

# print(res)

import itertools

nums = [1,2,3]
print(list(map(list, itertools.permutations(nums))))