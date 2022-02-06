import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
right = list(map(int, input().split()))
dy = [0]*n

for i in range(1, n+1):
    MAX = 0
    for j in range(right.index(i)-1, 0,-1):
        MAX = max(dy[j], MAX)
    dy[right.index(i)] = MAX + 1

print(max(dy))

