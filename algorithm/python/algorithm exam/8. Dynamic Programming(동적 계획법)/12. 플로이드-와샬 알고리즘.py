import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
dy = [["M"]*(n+1) for _ in range(n+1)]
for i in range(m):
    s, e, v = map(int, input().split())
    dy[s][e] = v
for i in range(1, n+1):
    dy[i][i] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dy[i][k] != "M" and dy[k][j] != "M":
                if dy[i][j] == "M":
                    dy[i][j] = dy[i][k] + dy[k][j]
                else:
                    dy[i][j] = min(dy[i][k] + dy[k][j], dy[i][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(dy[i][j], end=" ")
    print()




