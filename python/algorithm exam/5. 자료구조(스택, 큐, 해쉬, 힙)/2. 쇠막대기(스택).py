import sys
import os

os.chdir("C:\\python_study\\algorithm exam")
sys.stdin = open("input.txt", "r")

# razer = list(input())

# res = 0
# for idx, s in enumerate(razer):
#     cnt = r = 0
#     if s == '(' and razer[idx+1] != ')':
#         for i in range(idx+1, len(razer)):
#             if razer[i] == '(':
#                 cnt += 1

#             if razer[i] == ')' and razer[i-1] == '(':
#                 cnt -= 1
#                 r += 1
            
#             if razer[i] == ')' and razer[i-1] == ')':
#                 if cnt == 0:
#                     res += r+1
#                     break
#                 cnt -= 1

# print(res)


# 해답 코드
s = input()
stack = []
res = 0
for i in range(len(s)):
    stack.append(s[i])
    if stack[-1] == ')':
        if s[i-1] == '(':
            stack.pop()
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            stack.pop()
            res += 1

print(res)

    