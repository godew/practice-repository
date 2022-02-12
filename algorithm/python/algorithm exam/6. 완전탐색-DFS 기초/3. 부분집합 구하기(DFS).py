import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def PS(x, n, s):
    if x == n:
        print(" ".join(s))
        return
    s.append(str(x))
    PS(x+1, n, s)

    s.pop()
    PS(x+1, n, s)
    
def main():
    n = int(input())
    PS(1,n+1,[])

if __name__ == "__main__":
    main()


# 해답 코드

def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)