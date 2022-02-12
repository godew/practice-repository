import sys
import os

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def DFS(L, tot, day):
    global max_p
    if day>n:
        return
    if L == n+1:
        if tot>max_p:
            max_p = tot
        return
    if L > day:
        DFS(L+1, tot+sch[L][1], day+sch[L][0])
        DFS(L+1, tot, day+1)
    else:
        DFS(L+1, tot, day) 


if __name__ == "__main__":
    n = int(input())
    sch = [list(map(int, input().split())) for _ in range(n)]
    sch.insert(0,0)
    max_p = 0
    DFS(1, 0, 0)
    print(max_p)


# # 해답 코드
# def DFS(L, tot):
#     global max_p
#     if L > n+1:
#         return

#     if L == n+1:
#         if tot>max_p:
#             max_p = tot
#         return
    
#     DFS(L+sch[L][0], tot+sch[L][1])
#     DFS(L+1, tot)

# if __name__ == "__main__":
#     n = int(input())
#     sch = [list(map(int, input().split())) for _ in range(n)]
#     sch.insert(0,0)
#     max_p = 0
#     DFS(1, 0)
#     print(max_p)
