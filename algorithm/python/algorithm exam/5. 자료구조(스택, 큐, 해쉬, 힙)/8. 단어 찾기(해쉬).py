import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
poet = {}.fromkeys([input() for _ in range(n)], 0)
note = [input() for _ in range(n-1)]
for x in note:
    poet[x] = 1

for k, v in poet.items():
    if v==0:
        print(k)
        break
