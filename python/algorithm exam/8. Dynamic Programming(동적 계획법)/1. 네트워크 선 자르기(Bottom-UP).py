import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
dy = [1]*(n+1)
for i in range(2, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])


