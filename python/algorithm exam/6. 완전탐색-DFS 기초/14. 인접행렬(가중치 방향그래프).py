import sys
import os

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
res = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    inf = list(map(int, input().split()))
    res[inf[0]][inf[1]] = inf[2]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(res[i][j], end=" ")
    print()

