import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for b in a:
    b.insert(0, 0)
    b.append(0)
a.insert(0, [0]*(n+2))
a.append([0]*(n+2))

res = 0
for i in range(1, n+1):
     for j in range(1, n+1):
        if a[i][j] > a[i+1][j]:
            if a[i][j] > a[i-1][j]:
                if a[i][j] > a[i][j+1]:
                    if a[i][j] > a[i][j-1]:
                        res += 1
print(res)

# 해답 코드
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)