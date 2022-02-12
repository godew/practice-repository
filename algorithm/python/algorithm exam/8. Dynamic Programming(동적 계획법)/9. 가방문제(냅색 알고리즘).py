import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n, L = map(int, input().split())
jew = [list(map(int, input().split())) for _ in range(n)]
dy = [0]*1001

for i in range(L+1):
    dy[i] = 0
    for j in range(n):
        if i-jew[j][0] >= 0:
            dy[i] = max(dy[i-jew[j][0]] + jew[j][1], dy[i])

print(dy[L])

