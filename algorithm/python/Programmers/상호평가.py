def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def solution(scores):
    tmp = [] # 계산의 편의성을 위한 저장소
    leng = len(scores)
    res = ""
    for i in range(leng):
        for j in range(leng):
            tmp.append(scores[j][i])

    for i in range(leng):
        score = tmp[i*leng:(i + 1)*leng]
        if score[i] == max(score) or score[i] == min(score): # 최고점 or 최저점
            if score.count(score[i]) == 1: # 유일
                res += grade((sum(score) - score[i]) / (leng - 1))
                continue

        res += grade(sum(score) / leng)

    return res

print(solution([[70,49,90],[68,50,38],[73,31,100]]))