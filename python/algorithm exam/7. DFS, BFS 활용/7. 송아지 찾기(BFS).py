import sys
import os
from collections import deque

# os.chdir("C:\\python\\algorithm exam")
# sys.stdin = open("input.txt", "r")

def DFS():
    pass
    
if __name__ == "__main__":
    pass

# 해답 코드
s, e = map(int, input().split())
MAX = 10000
ch = [0]*(MAX+1)
dis = [0]*(MAX+1)
dQ = deque()
dQ.append(s)
ch[s] = 1
dis[s] = 0

while dQ:
    now = dQ.popleft()
    for next in (now-1, now+1, now+5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
            if next == e:
                print(dis[next])
                sys.exit(0)