import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "r")

L = int(input())
box = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    box.sort(reverse=True)
    box[0] -= 1
    box[L-1] += 1

box.sort(reverse=True)
print(box[0] - box[L-1])




	






