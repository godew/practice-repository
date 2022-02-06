import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

list_out = []
tc = int(input())
for _ in range(tc):
    list1 = []
    list2 = []
    n, s, e, k = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list1[s-1:e]
    list2.sort() # sort()함수는 return 값이 None이다.
    list_out.append(list2[k-1])

for i in range(tc):
    print("#{} {}".format(i+1, list_out[i]))

