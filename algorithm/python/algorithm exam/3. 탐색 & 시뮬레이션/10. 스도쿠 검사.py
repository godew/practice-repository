import sys
import os

# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

def is_sdoku(sdoku):
    tmp = set(range(1,10))
    
    for x in sdoku:
        if set(x) != tmp:
            return "NO"
    for j in range(9):
        Stmp = set()
        for i in range(9):
            Stmp.add(sdoku[i][j])
        if Stmp != tmp:
            return "NO"
    a = [0,1,2]; b = [3,4,5]; c = [6,7,8]
    for L1 in [a,b,c]:
        for L2 in [a,b,c]:
            Stmp = set()
            for i in L1:
                for j in L2:
                    Stmp.add(sdoku[i][j])
            if Stmp != tmp:
                return "NO"
    return "YES"


sdoku = [list(map(int, input().split())) for _ in range(9)]
print(is_sdoku(sdoku))

# 해답 코드
def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True






