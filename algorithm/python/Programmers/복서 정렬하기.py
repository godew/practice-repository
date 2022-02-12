def solution(weights, head2head):
    res = []
    for i in range(len(weights)):
        tmp = [] 
        tmp.append(i+1) # 번호
        tmp.append(weights[i]) # 몸무게
        if len(head2head[i]) - head2head[i].count("N") == 0:
            tmp.append(0)
        else:
            tmp.append(head2head[i].count("W") / (len(head2head[i]) - head2head[i].count("N"))) # 승률
        weight_win = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == "W" and weights[i] < weights[j]:
                weight_win += 1
        tmp.append(weight_win) # 몸무게가 많이나가는 선수를 이긴 횟수
        res.append(tmp)
    
    res.sort(key= lambda x : [-x[2], -x[3], -x[1], x[1]])
    return [x[0] for x in res]





print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))