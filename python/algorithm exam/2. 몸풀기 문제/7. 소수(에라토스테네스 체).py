import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

# def prime_check(x):
#     for i in range(2, x):
#         if x%i == 0:
#             return False
#     return True

# n = int(input())
# res = 0
# for i in range(2, n+1):
#     if prime_check(i):
#         res += 1
# print(res)

# n = int(input())
# a = []
# for i in range(2, n+1):
#     a.append(i)

# for x in a:
#     for y in a:
#         if y % x == 0 and y != x:
#             a.remove(y)
# print(len(a))

#해답 코드
n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
    for j in range(i, n+1, i):
        ch[j] = 1
print(cnt)

