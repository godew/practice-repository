import sys
import os
from collections import deque

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

def DFS():
    pass

if __name__ == "__main__":
    pass

n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
Q = deque()
Q.append([n//2, n//2])
ch[n//2][n//2] = 1
row = [-1,0,1,0]
col = [0,1,0,-1]
res = apple[n//2][n//2]

while True:
    root = Q.popleft()
    if root[0] == 0:
        break
    for i in range(4):
        if ch[root[0]+row[i]][root[1]+col[i]] == 0:
            Q.append([root[0]+row[i], root[1]+col[i]])
            ch[root[0]+row[i]][root[1]+col[i]] = 1
            res += apple[root[0]+row[i]][root[1]+col[i]]
print(res)
