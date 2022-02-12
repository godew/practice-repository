import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def PaskalVal(res):
    if len(res) == 1:
        return res[0]
    tmp = []
    for i in range(len(res)-1):
        tmp.append(res[i]+res[i+1])
    return PaskalVal(tmp)

def DFS(L):
    if L == n:
        if PaskalVal(res) == f:
            print(' '.join(map(str, res)))
            sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                res[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0
                
if __name__ == "__main__":
    n, f = map(int, input().split())
    res = [0] * n
    ch = [0] * (n+1)
    DFS(0)
    
    

