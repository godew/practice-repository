import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n = int(input())
tot_max = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if a==b and b==c:
        tot = 10000 + a*1000
    elif a==b or b==c or a==c:
        if a==b or b==c:
            tot = 1000 + b*100
        else:
            tot = 1000 + a*100
    else:
        tot = max(a,b,c)*100
    if tot_max < tot:
        tot_max = tot

print(tot_max)

