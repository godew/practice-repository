import itertools

def convert(op, expression):
    stack = []
    for tmp in expression:
        if tmp[-1].isdigit():
            if stack and stack[-1][-1].isdigit():
                stack[-1] = str(eval(stack[-1] + op + tmp))
            else:
                stack.append(tmp)
        else:
            if tmp != op:
                stack.append(tmp)
    return stack

            
def solution(expression):
    permu = list(itertools.permutations(["*","+","-"], 3))
    tmp = ""
    stack = []
    for ch in expression:
        if ch.isdigit():
            tmp += ch
        else:
            stack.append(tmp)
            stack.append(ch)
            tmp = ""
    stack.append(tmp)

    res = 0
    for prior in permu:
        res = max(res, abs(eval("".join(convert(prior[1],convert(prior[0], stack))))))
    
    return res

print(solution("50*6-3*2"))