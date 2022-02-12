import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "r")

def count(live, mid):
	i = cnt = 0
	tmp = mid
	while True:
		mid -= live[i]
		if mid == 0:
			cnt += 1
			mid = tmp
			if i == len(live)-1:
				break
		elif mid < 0:
			cnt += 1
			mid = tmp
			continue
		if i == len(live)-1:
			cnt += 1
			break
		i += 1
	return cnt

n, m = map(int, input().split())
live = list(map(int, input().split()))

lt = sum(live) // m ; rt = sum(live)
while lt <= rt:
	mid = (lt + rt) // 2
	if m >= count(live, mid):
		res = mid
		rt = mid - 1
	else:
		lt = mid + 1

print(res)
	