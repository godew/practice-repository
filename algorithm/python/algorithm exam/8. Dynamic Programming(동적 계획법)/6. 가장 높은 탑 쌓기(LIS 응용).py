import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
Info = [list(map(int, input().split())) for _ in range(n)]
Info.sort(reverse=True)
dy = [0]*n
for i in range(n):
    MAX = 0
    for j in range(i):
        if Info[i][2] < Info[j][2]:
            MAX = max(MAX, dy[j])
    dy[i] = MAX + Info[i][1]

print(max(dy))

