import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

tmp = []
for i in range(1, N+1):
    for j in range(1, M+1):
        tmp.append(i+j)
tmp.sort()

cnt = 1
res = []
max_cnt = float('-inf')
for i in range(len(tmp)-1):
    if tmp[i] == tmp[i+1]:
        cnt += 1
    elif max_cnt < cnt:
        max_cnt = cnt
        res.clear()
        res.append(tmp[i])
        cnt = 1
    elif max_cnt == cnt:
        res.append(tmp[i])
        cnt = 1
    else:
        cnt = 1

for i in res:
    print(i, end=" ")
    
# 해답 코드
cnt = [0]*(N+M-1)
max_cnt = float('-inf')
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j-2] += 1

for i in range(N+M-1):
    if max_cnt < cnt[i]:
        max_cnt = cnt[i]

for i in range(N+M-1):
    if max_cnt == cnt[i]:
        print(i+2, end=" ")
