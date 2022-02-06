import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
res = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        res += cnt
    else:
        cnt = 0
print(res)
        
