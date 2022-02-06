# import sys
# import os

# # os.chdir("C:\\python\\algorithm exam")
# # sys.stdin = open("input.txt", "r")


# def DFS(L):
#     global cnt
#     if L == m:
#         print(" ".join(map(str, res)))
#         cnt += 1
#     else:
#         for i in range(1, n+1):
#             if ch[i] == 0:
#                 for j in range(1,i+1):
#                     ch[j] = 1
#                 res[L] = i
#                 DFS(L+1)
#                 for j in range(1,i+1):
#                     ch[j] = 0



                
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     cnt = 0
#     res = [0]*m
#     ch = [0]*(n+1)
#     DFS(0)
#     print(cnt)


# # 해답 코드
# def DFS(L, s):
#     global cnt
#     if L==m:
#         for i in range(m):
#             print(res[i], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(s, n+1):
#             res[L]=i
#             DFS(L+1, i+1)
           
           

# n, m=map(int, input().split())
# res=[0]*(n+1)
# cnt=0
# DFS(0, 1)
# print(cnt)