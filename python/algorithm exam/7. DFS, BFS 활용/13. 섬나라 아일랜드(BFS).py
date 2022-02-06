import sys
import os
from collections import deque

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

def DFS(s):
    pass
if __name__ == "__main__":
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    Q = deque()
    res = 0

    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 1:
                Q.append([i,j])
                MAP[i][j] = 0
                while Q:
                    new = Q.popleft()
                    for k in range(8):
                        x = new[0] + dx[k]
                        y = new[1] + dy[k]
                        if 0 <= x <= n-1 and 0 <= y <= n-1 and MAP[x][y] == 1:
                            Q.append([x,y])
                            MAP[x][y] = 0
                res += 1
    
    print(res)


