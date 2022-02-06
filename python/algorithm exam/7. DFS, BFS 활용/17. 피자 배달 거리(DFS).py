import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def PDistance(tmp):
    pd = 0
    for x1,y1 in h:
        MIN = 2147000000
        for x2,y2 in tmp:
            MIN = min(MIN, abs(x1-x2) + abs(y1-y2))
        pd += MIN
    return pd

def DFS(L,s):
    global res
    if L == m:
        res = min(res, PDistance(tmp))

    else:
        for i in range(s, len(p)):
            tmp.append(p[i])
            DFS(L+1, i+1)
            tmp.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    p = []
    h = []
    tmp = []
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                p.append([i,j])
            if board[i][j] == 1:
                h.append([i,j])
    DFS(0,0)
    print(res)

