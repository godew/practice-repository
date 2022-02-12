def convert(p, res):
    if not p:
        return ""

    u = 0
    v = 0
    for i in range(len(p)):
        if p[i] == "(":
            u += 1
        else:
            v += 1

        if u == v:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    if u[0] == "(": # 올바른 괄호 문자열
        res = u + convert(v, res)
    else:
        res += "(" + convert(v, res) + ")"
        for ch in u[1:-1]:
            if ch == "(":
                res += ")"
            else:
                res += "("
    return res

def solution(p):
    return convert(p, "")
    
print(solution("(()())()"))
