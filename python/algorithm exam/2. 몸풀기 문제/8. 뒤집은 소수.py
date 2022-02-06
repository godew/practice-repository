import sys
import os
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")
def reverse(x):
    string = list(str(x))
    string.reverse()
    cnt = 0
    for i in string:
        if i == '0' and cnt == 0:
            string.remove('0')
        else:
            cnt = 1
    res = ""
    for c in string:
        res += c

    return int(res)
    
#해답 코드 함수
def reverse_sol(x):
    res = 0
    while x>0:
        t = x % 10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

for x in a:
    if isPrime(reverse(x)):
        print(reverse(x))

