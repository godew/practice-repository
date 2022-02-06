import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [500]*(m+1)
dy[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        dy[j] = min(dy[j], dy[j-coin[i]]+1)
print(dy[m])

