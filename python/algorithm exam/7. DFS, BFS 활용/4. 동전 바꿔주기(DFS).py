# import sys
# import os

# # os.chdir("C:\\python\\algorithm exam")
# # sys.stdin = open("input.txt", "r")

# def DFS(L, tot):
#     global res
#     if tot > T:
#         return
#     if L == k:
#         if tot == T:
#             res += 1
#     else:
#         for i in range(a[L][1]+1):
#             DFS(L+1, tot+a[L][0]*i)


# if __name__ == "__main__":
#     T = int(input())
#     k = int(input())
#     a = [list(map(int, input().split())) for _ in range(k)]
#     res = 0
#     DFS(0, 0)
#     print(res)

