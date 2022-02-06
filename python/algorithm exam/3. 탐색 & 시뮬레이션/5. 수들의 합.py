import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(i, n):
        if m == sum(a[i:j+1]):
            res += 1
            break
        elif m < sum(a[i:j+1]):
            break

print(res)

#해답 코드
n, m=map(int, input().split())
a=list(map(int, input().split()))

lt = 0
rt = 1
tot = a[lt]
res = 0
while True:
    if tot < m:
        if rt == n:
            break
        tot += a[rt]
        rt += 1
    elif tot == m:
        res += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(res)