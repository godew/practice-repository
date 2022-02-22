n = int(input())

res = []
for _ in range(n):
    res.append(int(input()))

res.sort()

for x in res:
    print(x)