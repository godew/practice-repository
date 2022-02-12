# import sys
# import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

# def DFS(i, tot, w_tot):

#     global max_w
#     if tot + w_sum - w_tot <= max_w:
#         return

#     if tot > c:
#         return
#     if i == n:
        
#         if max_w < tot:
#             max_w = tot

#     else:
#         DFS(i+1, tot+w[i], w_tot+w[i])
#         DFS(i+1, tot, w_tot+w[i])


# if __name__ == "__main__":


#     c, n = map(int, input().split())
#     w = [int(input()) for _ in range(n)]
#     w_sum = sum(w)

#     max_w = -2147000000
#     DFS(0, 0, 0)
#     print(max_w)


# # 해답 코드

# def DFS(L, sum, tsum):
#     global result
#     if sum+(total-tsum)<result:
#         return
#     if sum>c:
#         return
#     if L==n:
#         if sum>result:
#             result=sum
#     else:
#         DFS(L+1, sum+a[L], tsum+a[L])
#         DFS(L+1, sum, tsum+a[L])


# if __name__=="__main__":
#     c, n=map(int, input().split())
#     a=[0]*n
#     result=-2147000000
#     for i in range(n):
#         a[i]=int(input())
#     total=sum(a)
#     DFS(0, 0, 0)
#     print(result)



