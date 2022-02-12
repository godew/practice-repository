# import sys
# import os

# # os.chdir("C:\\python\\algorithm exam")
# # sys.stdin = open("input.txt", "r")

# def DFS(s):
#     global res
#     if s == e:
#         res += 1
#     else:
#         for i in range(4):
#             x = s[0]+dx[i]
#             y = s[1]+dy[i]
#             if 0 <= x <= n-1 and 0 <= y <= n-1:
#                 if MAP[s[0]][s[1]] < MAP[x][y]:
#                     DFS([x,y])



# if __name__ == "__main__":
#     n = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(n)]
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     s_min = 2147000000
#     e_max = -2147000000
#     for i in range(n): # 출발지 목적지 찾기
#         for j in range(n):
#             if s_min > MAP[i][j]:
#                 s_min = MAP[i][j]
#                 s =  [i,j]
#             if e_max < MAP[i][j]:
#                 e_max = MAP[i][j]
#                 e = [i,j]

#     res = 0
#     DFS(s)
#     print(res)
    

