import sys

n = int(input())
res = [0] * 10001
for _ in range(n):
    res[int(sys.stdin.readline())] += 1

for i in range(1, len(res)):
    for _ in range(res[i]):
        print(i)


