import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

def digit_sum(x):
    total = 0
    while x>0:
        total += x % 10 
        x = x // 10
    return total

def s_digit_sum(x): #해답 함수
    total = 0
    for i in str(x):
        total += int(i)
    return total

n = int(input())
list_data = list(map(int, input().split()))

max_list = float("-inf")
for idx, x in enumerate(list_data):
    if max_list < digit_sum(x):
        max_list = digit_sum(x)
        res = idx
print(list_data[res])
