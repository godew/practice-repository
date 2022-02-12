import math
def solution(progresses, speeds):
    days = []
    res = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    tmp = days[0]
    cnt = 0
    for day in days:
        if tmp < day:
            res.append(cnt)
            tmp = day
            cnt = 1
        else:
            cnt += 1
    else:
        res.append(cnt)
    
    return res

print(solution([93, 30, 55], [1, 30, 5]))