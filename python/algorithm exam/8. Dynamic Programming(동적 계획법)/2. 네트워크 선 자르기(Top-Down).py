import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def DFS(L):
    if dy[L] != 0:
        return dy[L]
    
    dy[L] = DFS(L-1) + DFS(L-2)
    return dy[L]

if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+2)
    dy[1] = 1
    dy[2] = 2
    print(DFS(n+1))


