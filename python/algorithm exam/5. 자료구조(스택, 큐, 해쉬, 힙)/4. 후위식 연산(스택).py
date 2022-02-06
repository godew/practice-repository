import sys
import os

# os.chdir("C:\\python_study\\algorithm exam")
# sys.stdin = open("input.txt", "r")

postfix = input()
stack = []

for x in postfix:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
            
        if x == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
            
        if x == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
            
        if x == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
            
print(stack[0])
