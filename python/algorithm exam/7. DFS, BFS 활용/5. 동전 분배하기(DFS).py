import sys
import os

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

def DFS(L, A_sum, B_sum, C_sum):
    global min_dif
    if L == 7:
        if A_sum != B_sum and A_sum != C_sum and B_sum != C_sum:
            if min_dif > max(A_sum, B_sum, C_sum) - min(A_sum, B_sum, C_sum):
                min_dif = max(A_sum, B_sum, C_sum) - min(A_sum, B_sum, C_sum)   
    else:
        DFS(L+1, A_sum+coin[L], B_sum, C_sum)
        DFS(L+1, A_sum, B_sum+coin[L], C_sum)
        DFS(L+1, A_sum, B_sum, C_sum+coin[L])


if __name__ == "__main__":
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    min_dif = 2147000000
    DFS(0,0,0,0)
    print(min_dif)

