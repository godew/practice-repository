import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

tot_max = -2147000000

for i in range(n):
    tot1 = tot2 = 0
    for j in range(n):
        tot1 += a[i][j]
        tot2 += a[j][i]
    if tot_max < tot1:
        tot_max = tot1
    if tot_max < tot2:
        tot_max = tot2
    
tot1 = tot2 = 0
for i in range(n):
    tot1 += a[i][i]
    tot2 += a[i][n-1-i]

if tot_max < tot1:
    tot_max = tot1
if tot_max < tot2:
    tot_max = tot2

print(tot_max)

