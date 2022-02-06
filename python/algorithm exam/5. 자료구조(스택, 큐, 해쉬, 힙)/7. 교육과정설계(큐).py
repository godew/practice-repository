import sys
import os
from  collections import deque

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

ess = input()
n = int(input())
Q = [input() for _ in range(n)]

for i, s in enumerate(Q):
    s = deque(s)
    for _ in range(len(s)):
        if s[0] in ess:
            s.append(s.popleft())
        else:
            s.popleft()
    
    if "".join(s) == ess:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))

