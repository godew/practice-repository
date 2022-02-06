# import sys
# import os

# # os.chdir("C:\\python\\algorithm exam")
# # sys.stdin = open("input.txt", "r")

# def DFS(tot, t, s):
#     global max_tot
#     if t > m:
#         return
#     if max_tot < tot:
#         max_tot = tot
#     for i in range(s, n):
#         DFS(tot+a[i][0], t+a[i][1], i+1)


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     a = [list(map(int, input().split())) for _ in range(n)]

#     max_tot = 0
#     DFS(0, 0, 0)
#     print(max_tot)
        


# # 해답 코드
# def DFS(L, sum, time):
#     global res
#     if time>m:
#         return
#     if L==n:
#         if sum>res:
#             res=sum
#     else:
#         DFS(L+1, sum+pv[L], time+pt[L])
#         DFS(L+1, sum, time)

# if __name__=="__main__":
#     n, m=map(int, input().split())
#     pv=list()
#     pt=list()
#     for i in range(n):
#         a, b=map(int, input().split())
#         pv.append(a)
#         pt.append(b)
#     res=-2147000000
#     DFS(0, 0, 0)
#     print(res)