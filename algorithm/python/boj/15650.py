# def combination(L, k):
#     if L == m:
#         print(*res)
#         return

#     for i in range(k+1, n+1):
#         res.append(i)
#         combination(L+1, i)
#         res.pop()

# n, m = map(int, input().split())
# res = []

# combination(0, 0)

from itertools import combinations

n, m = map(int, input().split())
for tuple_ in combinations(range(1, n+1), m):
    print(*tuple_)