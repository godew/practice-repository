import sys
import os
from collections import deque

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

def DFS():
    pass

if __name__ == "__main__":
    m, n = map(int, input().split())
    toma = [list(map(int, input().split())) for _ in range(n)]
    res = -1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    Q = deque()
    for i in range(n):
        for j in range(m):
            if toma[i][j] == 1:
                Q.append([i,j])
    Q.append(0)
    while Q:
        new = Q.popleft()
        if new == 0:
            if len(Q) == 0:
                res += 1
                break
            Q.append(0)
            res += 1
            continue
        for i in range(4):
            x = new[0] + dx[i]
            y = new[1] + dy[i]
            if 0<=x<=n-1 and 0<=y<=m-1 and toma[x][y]==0:
                toma[x][y] = 1
                Q.append([x,y])
                
    for i in range(n):
        for j in range(m):
            if toma[i][j] == 0:
                print(-1)
                sys.exit(0)
    print(res)








    





    

