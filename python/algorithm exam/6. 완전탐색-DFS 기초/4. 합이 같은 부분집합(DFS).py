import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def DFS(x):
    if x > n-1:
        total = 0
        for i in range(n):
            total += a[i] * ch[i]
        
        if total == 0:
            print("YES")
            sys.exit(0) # 시스템 종료

    else:
        ch[x] = 1
        DFS(x+1)
        ch[x] = -1
        DFS(x+1)



if __name__ == "__main__":

    n = int(input())
    a = list(map(int, input().split()))
    ch = [0]*n
    DFS(0)
    print("NO")


