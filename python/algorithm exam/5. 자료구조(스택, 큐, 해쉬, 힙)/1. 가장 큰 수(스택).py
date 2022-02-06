import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
n = str(n)
a = len(n) - m

tmp = []; res = []
for c in n:
    tmp.append(int(c))
# n =list(map(int, str(n)))
while m:
    max_val = -2147000000
    for i, val in enumerate(tmp):
        if i == m+1:
            break
        if max_val < val:
            max_val = val
            idx = i
    m -= idx
    for i in range(idx):
        tmp.pop(0)

    if len(res) == a:
        break

    res.append(tmp.pop(0))


if len(res) == a:
    for x in res:
        print(x, end="")
else:
    res = res+tmp
    for x in res:
        print(x, end="")


# 해답 코드
num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)

    




    




    




