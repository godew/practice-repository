def permutation(L):
    if L == m:
        print(*res)
        return

    for i in range(1, n+1):
        if ch[i] == 0:
            res.append(i)
            ch[i] = 1
            permutation(L+1)
            res.pop()
            ch[i] = 0

n, m = map(int, input().split())
ch = [0]*(n+1)
res = []

permutation(0)

from itertools import permutations

n, m = map(int, input().split())
for tuple_ in permutations(range(1, n+1), m):
    print(*tuple_)