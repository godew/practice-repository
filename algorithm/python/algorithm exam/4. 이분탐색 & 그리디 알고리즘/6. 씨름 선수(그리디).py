import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
body = [list(map(int, input().split())) for _ in range(n)]
body.sort(reverse=True)


lweight = []
res = 0
for L in body:
	lweight.append(L[1])
	if L[1] == max(lweight):
		res += 1
print(res)








	






