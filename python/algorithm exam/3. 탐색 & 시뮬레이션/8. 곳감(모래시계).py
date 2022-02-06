import sys
import os
import copy

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    b = list(map(int, input().split()))
    tmp = copy.deepcopy(a[b[0]-1])
    if b[1] == 0: 
        for i in range(n):
            a[b[0]-1][i-b[2]%n] = tmp[i]
    if b[1] == 1: 
        for i in range(n):
            a[b[0]-1][i+b[2]%n-n] = tmp[i]

s = 0 ; e = n-1
res = 0
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i >= n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
            
# 해답 코드
for i in range(m):
    h, t, k=map(int, input().split())
    if(t==0):
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())