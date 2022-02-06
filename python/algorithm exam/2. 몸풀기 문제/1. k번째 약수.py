import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

while True:
    n, k = map(int, input().split())
    if 1<=n<=10000:
        if 1<=k<=n:
            break
    else:
        print("재입력하세요.")

cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)




