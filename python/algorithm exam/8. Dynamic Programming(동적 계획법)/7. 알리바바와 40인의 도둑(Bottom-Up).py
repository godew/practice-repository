import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n= int(input())
stone = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]

dy[0][0] = stone[0][0]
for j in range(1, n):
        dy[0][j] = dy[0][j-1]+stone[0][j]
        dy[j][0] = dy[j-1][0]+stone[j][0]

for i in range(1, n):
    for j in range(i, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + stone[i][j]
        dy[j][i] = min(dy[j-1][i], dy[j][i-1]) + stone[j][i]
    
print(dy[n-1][n-1])

