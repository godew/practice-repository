def find(parent, node): # 부모 노드 찾는다
    if parent[node] == node:
        return node
    return find(parent, parent[node])

def union(parent, node1, node2): # 두 노드 합친다
    p1 = find(parent, node1)
    p2 = find(parent, node2)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

def solution(n, costs):
    costs.sort(key= lambda x : x[2])
    parent = [i for i in range(n)]

    cnt = 0
    res = 0
    for cost in costs:
        if find(parent, cost[0]) == find(parent, cost[1]): #cycle
            continue
        else:
            union(parent, cost[0], cost[1])
            cnt += 1
            res += cost[2]
        
        if cnt == n-1:
            return res

print(solution(7, [[0,1,7],[1,2,8],[0,3,5],[3,1,9],[4,1,7],[3,4,15],[3,5,6],[4,5,8],[6,5,11],[6,4,9],[2,4,5]]))

