import sys
import os
import copy
# os.chdir("C:\\python_study\\Exam")
# sys.stdin = open("input.txt", "rt")

def reverse(card, ai, bi):
    tmp = card[ai-1:bi]
    tmp.reverse()
    for i in range(ai-1, bi):
        card[i] = tmp[i-ai+1]

card = list(range(21))
card.remove(0)

for _ in range(10):
    ai, bi = map(int, input().split())
    reverse(card, ai, bi)

for x in card:
    print(x, end=" ")

# #해답 코드
# for _ in range(10):
#     s, e=map(int, input().split())
#     for i in range((e-s+1)//2):
#         a[s+i], a[e-i]=a[e-i], a[s+i] # a,b = b,a
