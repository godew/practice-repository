def DFS(i, computers, computer):
    for j, v in enumerate(computer):
        if v == 1: # 다른 노드와 연결되어있으면
            computers[i][j] = 0
            computers[j][i] = 0
            computers[j][j] = 0 
            DFS(j, computers, computers[j])

def solution(n, computers):
    res = 0
    for i, computer in enumerate(computers):
        if computers[i][i] == 1: # 탐색하지 않은 node면 DFS한다
            computers[i][i] = 0
            DFS(i, computers, computer)
            res += 1
    return res

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))