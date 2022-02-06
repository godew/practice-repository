import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "r")

n = int(input())
conf = [list(map(int, input().split())) for _ in range(n)]

min_div = 2147000000
# lt, rt 초기화
for L in conf:
	if min_div > L[1] - L[0] :
		min_div = L[1] - L[0]
		lt = L[0]; rt = L[1]

res = 1
lflag = True; rflag = True
tmp_lt = lt; tmp_rt = rt
while True:
	# left
	if lflag:
		min_div = 2147000000
		for L in conf:
			if min_div > lt - L[0] and L[1] <= lt:
				min_div = lt - L[0]
				tmp_lt = L[0]

		if lt != tmp_lt:
			res += 1
			lt = tmp_lt
		else:
			lflag = False
		
	# right
	if rflag:
		min_div = 2147000000
		for L in conf:
			if min_div > L[1] - rt and L[0] >= rt:
				min_div = L[1] - rt
				tmp_rt = L[1]
		
		if rt != tmp_rt:
			res += 1
			rt = tmp_rt
		else:
			rflag = False

	if not(lflag or rflag):
		break

print(res)

# 해답 코드

n = int(input())
conf = [list(map(int, input().split())) for _ in range(n)]

conf.sort(key = lambda x : x[1])

et = 0
res = 0
for L in conf:
	if et <= L[0]:
		et = L[1]
		res += 1
print(res)







	






