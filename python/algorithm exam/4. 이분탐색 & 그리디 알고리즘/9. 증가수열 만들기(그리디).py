import sys
import os
from collections import deque

os.chdir("C:\\python_study\\algorithm exam")
sys.stdin = open("input.txt", "r")

n = int(input())
nlist = deque(map(int, input().split()))

res_str = ""
tmp = 0
while nlist:

    if tmp > nlist[0] and tmp > nlist[-1]:
            break
    elif tmp < nlist[0] and tmp < nlist[-1]:
        if nlist[0] <= nlist[-1]:
            tmp = nlist.popleft()
            res_str += "L"
        else:
            tmp = nlist.pop()
            res_str += "R"
    elif tmp < nlist[0] and tmp > nlist[-1]:
        tmp = nlist.popleft()
        res_str += "L"
    else:
        tmp = nlist.pop()
        res_str += "R"

print(len(res_str))
print(res_str)
    
    
    




