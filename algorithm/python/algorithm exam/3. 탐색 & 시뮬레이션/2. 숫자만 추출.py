import sys
import os
import copy
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

def divisor(n):
    res = 0
    for i in range(1, n+1):
        if n%i == 0:
            res += 1
    return res

def extraction(s):
    tmp = ["1","2","3","4","5","6","7","8","9","0"]
    res = 0
    for s1 in s: 
       if s1 in tmp:
           res = res*10 + int(s1)
    return res

s = input()
print(extraction(s))
print(divisor(extraction(s)))


#해답 코드
for x in s:
    if x.isdecimal(): #isdecimal() = 십진수문자(0~9)로 이루어진 문자열이 오면 True반환
        res=res*10+int(x)
print(res)
