def solution(routes):
    routes.sort(key= lambda x : x[1])
    ch = [0]*len(routes)
    res = 0

    for idx in range(len(routes)):
        if ch[idx] == 0:
            res += 1
            ch[idx] = 1
            for i in range(idx+1, len(routes)):
                if ch[i] == 0 and routes[i][0] <= routes[idx][1]:
                    ch[i] = 1
    
    return res



print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))