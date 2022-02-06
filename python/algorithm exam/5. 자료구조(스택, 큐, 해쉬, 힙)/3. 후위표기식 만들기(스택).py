import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

postfix = list(input())
stack = []
cal_stack = []

i = 0
while i<len(postfix):
    if not postfix[i].isdecimal():
        if cal_stack:
            top = cal_stack[-1]
            if top in ("-", "+") and postfix[i] in ("-", "+"):
                stack.append(cal_stack.pop(-1))

        cal_stack.append(postfix[i])

        if postfix[i] in ("*", "/"):
            if postfix[i+1].isdecimal():
                stack.append(postfix[i+1])
                stack.append(cal_stack.pop())
                i += 1

        if postfix[i] == ")":
            while True:
                tmp = cal_stack.pop()
                if tmp == "(":
                    break
                if tmp not in ("(", ")"):
                    stack.append(tmp)
            if cal_stack and cal_stack[-1] in ("*", "/"):
                stack.append(cal_stack.pop())

    else:
        stack.append(postfix[i])

    i += 1

cal_stack.reverse()
stack = stack + cal_stack
print("".join(stack))


# 해답 코드
a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
