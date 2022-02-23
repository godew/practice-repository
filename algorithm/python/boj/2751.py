import sys
n = int(input())

res = []
for _ in range(n):
    res.append(int(sys.stdin.readline()))

res.sort()

for x in res:
    print(x)