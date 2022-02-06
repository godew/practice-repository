# import sys
# import os

# # os.chdir("C:\\python\\algorithm exam")
# # sys.stdin = open("input.txt", "r")

# def DFS(L, tot):
#     global res_min

#     if L >= res_min:
#         return 
#     if tot > m:
#         return 
#     elif tot == m:
#         if res_min > L:
#             res_min = L
#             return
#     else:
#         for x in kind:
#             DFS(L+1, tot+x)
    

# if __name__ == "__main__":

#     n = int(input())
#     kind = list(map(int, input().split()))
#     kind.sort(reverse=True)
#     m = int(input())
#     res_min = 2147000000
#     DFS(0, 0)
#     print(res_min)

