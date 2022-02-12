import sys
import os
import heapq as hq

os.chdir("C:\\python_study\\algorithm exam")
sys.stdin = open("input.txt", "r")

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)


 





