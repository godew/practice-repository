# import sys
# import os
# from collections import deque

# # os.chdir("C:\\python\\algorithm exam")
# # sys.stdin = open("input.txt", "r")

# def BFS(s):
#     Q = deque()
#     Q.append(s)
#     a = []
#     while Q:
#         new = Q.popleft()
#         for i in range(4):
#             x = new[0]+dx[i]
#             y = new[1]+dy[i]
#             if 0 <= x <= n-1 and 0<= y <= n-1:
#                 if MAP[x][y] == "1":
#                     if ch[x][y] == 0:
#                         ch[x][y] = res_num
#                         Q.append([x,y])
#                         res[-1] += 1
#                 else:
#                     a.append([x,y])
#     return a

# def DFS(s):
#     global res_num

#     for i in range(4):
#         x = s[0]+dx[i]
#         y = s[1]+dy[i]
#         if 0 <= x <= n-1 and 0<= y <= n-1 and ch[x][y] == 0:
#             if MAP[x][y] == "1":
#                 res_num += 1
#                 ch[x][y] = res_num
#                 res.append(1)
#                 for b in BFS([x,y]):
#                     DFS(b)
#             else:
#                 ch[x][y] = -1
#                 DFS([x,y])


# if __name__ == "__main__":
#     n = int(input())
#     MAP = [list(input()) for _ in range(n)]
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     ch = [[0]*n for _ in range(n)]
#     res = []
#     res_num = 0

#     if MAP[0][0] == "1":
#         res_num += 1
#         ch[0][0] = res_num
#         res.append(1)
#         for b in BFS([0,0]):
#             DFS(b)
#     else:
#         ch[0][0] = -1
#         DFS([0,0])
#     res.sort()
#     print(res_num)
#     for x in res:
#         print(x)



# # 해답 코드

# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]

# def DFS(x, y):
#     global cnt
#     cnt+=1
#     board[x][y]=0
#     for i in range(4):
#         xx=x+dx[i]
#         yy=y+dy[i]
#         if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
#             DFS(xx, yy)

# if __name__=="__main__":
#     n=int(input())
#     board=[list(map(int, input())) for _ in range(n)]
#     res=[]
#     for i in range(n):
#         for j in range(n):
#             if board[i][j]==1:
#                 cnt=0
#                 DFS(i, j)
#                 res.append(cnt)
#     print(len(res))
#     res.sort()
#     for x in res:
#         print(x)

