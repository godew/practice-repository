def solution(people, limit):
    res = 0
    lt = 0
    rt = len(people)-1
    people.sort()
    while lt < rt:
        if people[lt] + people[rt] > limit:
            rt -= 1
            res += 1
        else:
            lt += 1
            rt -= 1
            res += 1
    else:
        if lt == rt:
            res += 1
    
    return res
        

print(solution([70, 50, 80, 50], 100))