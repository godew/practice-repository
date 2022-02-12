# import sys
# import os

# # os.chdir("C:\\python\\algorithm exam")
# # sys.stdin = open("input.txt", "r")

# def DFS(x,y):
#     global res
#     if x == 6 and y == 6:
#         res += 1
#     else:
#         for i in range(4):
#             if 0<=x+dx[i]<=6 and 0<=y+dy[i]<=6:
#                 if miro[x+dx[i]][y+dy[i]] == 0:
#                     miro[x+dx[i]][y+dy[i]] = 1
#                     DFS(x+dx[i], y+dy[i])
#                     miro[x+dx[i]][y+dy[i]] = 0


# if __name__ == "__main__":
#     miro = [list(map(int, input().split())) for _ in range(7)]
#     res = 0 
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     miro[0][0] = 1
#     DFS(0,0)

#     print(res)

