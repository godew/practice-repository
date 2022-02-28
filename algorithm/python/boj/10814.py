import sys
n = int(input())
res = []

for _ in range(n):
    res.append(sys.stdin.readline().split())

res.sort(key= lambda x : int(x[0]))
for x in res:
    print(x[0], x[1])