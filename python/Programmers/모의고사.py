def chaejum(jjik, answers):
    sp = list(zip(answers, jjik * 1500))
    res = 0
    for x, y in sp:
        if x == y:
            res += 1
    return res

def solution(answers):

    tmp = []
    tmp.append(chaejum([1,2,3,4,5,1,2,3,4,5], answers))
    tmp.append(chaejum([2,1,2,3,2,4,2,5], answers))
    tmp.append(chaejum([3,3,1,1,2,2,4,4,5,5], answers))

    res = []
    max_p = max(tmp)
    for i, p in enumerate(tmp):
        if p == max_p:
            res.append(i+1)

    return res