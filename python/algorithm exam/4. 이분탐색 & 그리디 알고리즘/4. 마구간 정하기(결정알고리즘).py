import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "r")

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

lt = 1; rt = house[n-1] - house[0]

while lt <= rt:
	start = house[0]
	cnt = 1
	mid = (lt+rt)//2
	for i in range(len(house)):
		if house[i] - start >= mid:
			start = house[i]
			cnt += 1

	if cnt >= c:
		lt = mid + 1
		res = mid
	else:
		rt = mid - 1

print(res)










	






