def solution(s):
    answer = len(s)
    for div in range(1, len(s)//2 + 1):
        res = []
        cnt = 1
        for i in range(0, len(s), div):
            tmp = s[i:i+div]
            if res and res[-1] == tmp:
                cnt += 1
            else:
                if cnt != 1:
                    res.append(str(cnt))
                res.append(tmp)
                cnt = 1
        if cnt != 1:
            res.append(str(cnt))
        answer = min(answer, len("".join(res)))
        
    return answer


print(solution("abcabcabcabcdededededede"))