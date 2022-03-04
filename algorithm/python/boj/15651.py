def permutation(L):
    if L == m:
        print(*res)
        return

    for i in range(1, n+1):
        res.append(i)
        permutation(L+1)
        res.pop()

n, m = map(int, input().split())
res = []

permutation(0)
