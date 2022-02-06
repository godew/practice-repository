import sys
import os
from collections import deque

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

def DFS():
    pass

if __name__ == "__main__":
    pass

miro = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
Q = deque()
Q.append([0,0])
miro[0][0] = 1
dis[0][0] = 0
res = 0
while Q:
    pn = Q.popleft()
    for i in range(4):
        if 0 <= pn[0]+dx[i] <= 6 and 0 <= pn[1]+dy[i] <= 6:
            if miro[pn[0]+dx[i]][pn[1]+dy[i]] == 0:
                miro[pn[0]+dx[i]][pn[1]+dy[i]] = 1
                Q.append([pn[0]+dx[i], pn[1]+dy[i]])
                dis[pn[0]+dx[i]][pn[1]+dy[i]] = dis[pn[0]][pn[1]] + 1
                if pn[0]+dx[i] == 6 and pn[1]+dy[i] == 6:
                    print(dis[pn[0]+dx[i]][pn[1]+dy[i]])
                    sys.exit(0)
else:
    print(-1)
                    
