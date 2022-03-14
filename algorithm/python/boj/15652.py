def permutation(L, k):
    if L == m:
        print(*res)
        return

    for i in range(k, n+1):
        res.append(i)
        permutation(L+1, i)
        res.pop()

n, m = map(int, input().split())
res = []

permutation(0, 1)
