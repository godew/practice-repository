import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
dy = [[100]*(n+1) for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    dy[a][b] = 1
    dy[b][a] = 1

for i in range(1, n+1):
    dy[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dy[i][j] = min(dy[i][k] + dy[k][j], dy[i][j])

res = [100]*(n+1)
for i in range(1, n+1):
    dy[i].sort(reverse=True)
    res[i] = dy[i][1]


print(min(res), res.count(min(res)))
for i, x in enumerate(res):
    if x == min(res):
        print(i, end=" ")

