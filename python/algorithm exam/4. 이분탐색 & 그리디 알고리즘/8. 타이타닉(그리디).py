import sys
import os
from copy import deepcopy
# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort(reverse=True)

res = 0
while weight:

    a = weight.pop(0)
    # a = weight.pop(0) 0번 인덱스 빼주면 뒤에 자료들이 앞으로 당겨져서 비효율적이다
    # deque
    # a = weight.popleft() 0번인덱스 pop해준 후 포인터가 그다음 자료를 가리킨다. 그래서 효율적

    tmp = deepcopy(weight)
    tmp.sort()
    max_y = 0
    for y in tmp:
        if M-a > y:
            if max_y < y:
                max_y = y
        elif M-a == y:
            max_y = y
            break
        else:
            break
    res += 1
    if max_y == 0:
        continue
    else:
        weight.remove(max_y)
print(res)
 
