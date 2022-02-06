import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

def left_top(l):
    res = 0
    for i in range(n//2):
        for j in range(i+1):
            res += l[j][i-j]
    return res

n = int(input())
app = [list(map(int, input().split())) for _ in range(n)]

total = 0
for l in app:
    total += sum(l)

res = 0
res += left_top(app)

for l in app:
    l.reverse()

res += left_top(app)

for i in range(n):
    for j in range(n//2):
        app[j][i], app[n-j-1][i] = app[n-j-1][i],  app[j][i]

res += left_top(app)

for l in app:
    l.reverse()

res += left_top(app)

print(total - res)

#해답 코드
res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += app[i][j]
    if i >= n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
