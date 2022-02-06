import sys
import os

os.chdir("C:\\python_study\\algorithm exam")
sys.stdin = open("input.txt", "r")

a = list(input())
b = list(input())
dic_a = {}
dic_b = {}

while a: 
    tmp = a[0]
    dic_a[tmp] = a.count(tmp)
    for _ in range(a.count(tmp)):
        a.pop(a.index(tmp))

while b: 
    tmp = b[0]
    dic_b[tmp] = b.count(tmp)
    for _ in range(b.count(tmp)):
        b.pop(b.index(tmp))

if dic_a == dic_b:
    print("YES")
else:
    print("NO")

# # 해답 코드

a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x]=str1.get(x, 0)+1
for x in b:
    str2[x]=str2.get(x, 0)+1

if str1 == str2:
    print("YES")
else:
    print("NO")

# 리시트 해쉬

a=input()
b=input()
str1=[0]*52
str2=[0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")





