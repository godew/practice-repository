import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "r")

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

lt = 1; rt = max(lan)
res = 0
while lt <= rt:
	mid = (lt+rt) // 2
	cnt = 0 
	for x in lan:
		cnt += x//mid
	if cnt >= n:
		res = mid
		lt = mid+1
	else:
		rt = mid-1

print(res)


