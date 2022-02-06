import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
rev = list(map(int, input().split()))
tmp = list(range(1,n+1))
rev.reverse()
tmp.reverse() 
res = []

for i in range(n):
    res.insert(rev[i],tmp[i])

for x in res:
    print(x, end=" ")
    




    




