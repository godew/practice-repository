import sys
import os
import copy

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

def ismoonsu(l):
    tmp = copy.deepcopy(l)
    tmp.reverse()
    if l == tmp:
        return True

a = [list(map(int, input().split())) for _ in range(7)]

res = 0
for i in range(7):
    for k in range(3):
        l1 = []
        l2 = [] 
        cnt = 0
        for j in range(7):
            l1.append(a[i][j+k])
            l2.append(a[j+k][i])
            cnt += 1
            if cnt == 5:
                break
        if ismoonsu(l1):
            res += 1
        if ismoonsu(l2):
            res += 1

print(res)
