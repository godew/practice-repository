from collections import defaultdict
def solution(n, lost, reserve):
    # 무조건 제일 가까운애한테 주면 된다.
    tmp = defaultdict(int)
    res = n - len(lost)

    for x in lost:
        tmp[x] += 1
    for x in reserve:
        if tmp[x] == 1:
            res += 1
            tmp.pop(x)

    tmp = sorted(tmp.items())
    
    i = 0
    while i < len(tmp)-1:
        if tmp[i][1] != tmp[i+1][1] and (tmp[i+1][0] - tmp[i][0]) == 1:
            i += 2
            res += 1
        else:
            i += 1
    
    return res


print(solution(5, [2, 4], [1, 3, 5]))