import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def DFS(x, s):
    res[x] = 1
    for i in range(s, len(w)):
        DFS(x+w[i], i+1)
        DFS(abs(x-w[i]), i+1)
    
if __name__ == "__main__":
    k = int(input())
    w = list(map(int, input().split()))
    res = [0]*(sum(w)+1)
    DFS(0,0)
    print(res.count(0))