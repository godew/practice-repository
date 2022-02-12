# import sys
# import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

# def DFS(x):
#     global cnt
#     if x == m:
#         for i in range(m):
#             print(res[i], end=" ")
#         res[m-1] = 0
#         cnt += 1
#         print()
#     else:
#         for i in range(1, n+1):
#             if i not in res:
#                 res[x] = i
#                 DFS(x+1)
        

# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     res = [0]*m
#     cnt = 0
#     DFS(0)
#     print(cnt)


