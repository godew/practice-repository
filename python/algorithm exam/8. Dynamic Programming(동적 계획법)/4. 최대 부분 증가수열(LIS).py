import sys
import os

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
dy = [0]*n

for i in range(n):
    MAX = 0
    for j in range(i):
        if arr[i] > arr[j]:
            MAX = max(MAX, dy[j])
    dy[i] = MAX+1

print(max(dy))

 