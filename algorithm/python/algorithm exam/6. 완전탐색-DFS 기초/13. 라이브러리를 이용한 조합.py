import sys
import os
import itertools as it # 순열과 조합을 자동으로 구해준다.

os.chdir("C:\\python\\algorithm exam")
sys.stdin = open("input.txt", "r")

n, f=map(int, input().split())
p=[0]*n
b=[1]*n
for i in range(1, n):
    b[i]=b[i-1]*(n-i)//i
a = list(range(1, n+1))
print(a)
for tmp in it.permutations(a, 3): # 순열 -> a중에 3개를 뽑아 순열해라
    print(tmp)