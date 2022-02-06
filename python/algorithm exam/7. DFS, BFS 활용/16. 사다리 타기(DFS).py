import sys
import os
import copy

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

def DFS(x,y):
    if x == 9:
        if tmp[x][y] == 2:
            print(k)
            sys.exit(0)

    for i in range(3):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<=9 and 0<=yy<=9 and tmp[x][y] != 0 and (tmp[xx][yy] == 1 or tmp[xx][yy] == 2):
            tmp[x][y] = 0
            DFS(xx,yy)




if __name__ == "__main__":
    ladder = [list(map(int, input().split())) for _ in range(10)]
    dx = [0,0,1]
    dy = [1,-1,0]
    for k in range(10):
        tmp = copy.deepcopy(ladder)
        DFS(0,k)
        
        








    





    

