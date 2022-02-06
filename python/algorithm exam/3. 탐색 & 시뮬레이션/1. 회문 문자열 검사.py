import sys
import os
import copy
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

def ghlmoon(s):
    
    s = list(s.lower())
    tmp = copy.deepcopy(s) # list 복사할때 데이터만 넘기려면 깊은복사해야한다.
    tmp.reverse()

    if tmp == s:
        return "YES"
    else:
        return "NO"

n = int(input())
for i in range(n):
    s = input()
    print("#{} {}".format(i+1, ghlmoon(s)))

#해답 코드
for i in range(n):
    s=input()
    s=s.upper()
    if s==s[::-1]:
        print("#%d YES" %i)
    else:
        print("#%d NO" %i)