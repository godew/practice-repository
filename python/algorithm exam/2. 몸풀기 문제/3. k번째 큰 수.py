import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

cnt = 0
idx = 0
num, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = []
for i in range(num-2):
    for j in range(i+1, num-1):
        for m in range(j+1, num):
            list2.append(list1[i] + list1[j] + list1[m])
list2.sort(reverse=True)

while True:
    if list2[idx] == list2[idx+1]:
        idx += 1
        continue
    idx += 1
    cnt += 1
    if k == cnt:
        print(list2[idx-1])
        break
    
#해답코드
# n, k=map(int, input().split())
# a=list(map(int, input().split()))
# res=set() # set()는 중복을 제거하는 자료구조
# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             res.add(a[i]+a[j]+a[m])
# res=list(res)
# res.sort(reverse=True)
# print(res[k-1])

