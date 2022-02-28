import sys
n = int(input())
res = {}

tmp = list(map(int, sys.stdin.readline().split()))
set_ = set(tmp)
for i, x in enumerate(sorted(set_)):
    res[x] = i

for x in tmp:
    print(res[x], end=" ")


