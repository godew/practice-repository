import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b =  list(map(int, input().split()))

# res = a + b
# res.sort()
# for i in range(n1+n2):
#     print(res[i], end=" ")

# sort() -> nlogn 복잡도 (퀵정렬)
# 이 문제는 n번만에 가능하다

p1, p2 = 0, 0
c = []
for i in range(n1+n2):
    if a[p1] >= b[p2]:
        c.append(b[p2])
        if p2 == n2-1:
            c.extend(a[p1:])
            break
        p2 += 1
    else:
        c.append(a[p1])
        if p1 == n1-1:
            c.extend(b[p2:])
            break
        p1 += 1

for x in c:
    print(x, end=" ")

# 해답 코드
# p1=p2=0
# c=[]
# while p1<n and p2<m: 
#     if a[p1]<b[p2]:
#         c.append(a[p1])
#         p1+=1
#     else:
#         c.append(b[p2])
#         p2+=1
# if p1<n:
#     c=c+a[p1:]
# if p2<m:
#     c=c+b[p2:]
# for x in c:
#     print(x, end=' ')