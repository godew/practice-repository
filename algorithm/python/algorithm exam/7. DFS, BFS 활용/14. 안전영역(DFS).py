import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def DFS(s):
    for i in range(4):
        x = s[0] + dx[i]
        y = s[1] + dy[i]
        if 0 <= x <= n-1 and 0 <= y <= n-1 and ch[x][y] == 1:
            ch[x][y] = 0
            DFS([x,y])


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    res = 0
    MAX = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > MAX:
                MAX = area[i][j]   
    rain = MAX

    for r in range(rain):
        for i in range(n):
            for j in range(n):
                if area[i][j] > r:
                    ch[i][j] = 1
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 1:
                    ch[i][j] = 0
                    DFS([i,j])
                    cnt += 1
        if res < cnt:
            res = cnt
    print(res)






    





    

