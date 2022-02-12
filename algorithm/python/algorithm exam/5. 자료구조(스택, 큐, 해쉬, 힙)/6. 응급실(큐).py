import sys
import os
from  collections import deque

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
risk = deque(map(int, input().split()))

res = 0
while risk:
    if max(risk) > risk[0]:
        risk.append(risk.popleft())
        if m == 0:
            m = len(risk) - 1
            continue

    else:
        risk.popleft()
        res += 1
        if m == 0:
            print(res)
            break

    m -= 1


# 해답 코드

n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]  # 인덱스도 그냥 같이 지정
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
