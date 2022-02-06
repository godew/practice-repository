def solution(tickets):
    tickets.sort(key= lambda x : x[1])
    res = ["ICN"]
    ch = [0]*len(tickets)
    def DFS(begin, L):
        if L == len(tickets):
            return -1
        for i, ticket in enumerate(tickets):
            if ch[i] == 0 and ticket[0] == begin:
                res.append(ticket[1])
                ch[i] = 1
                if DFS(ticket[1], L+1) < 0:
                    return -1
                res.pop()
                ch[i] = 0
        return 1

    DFS("ICN", 0)
    return res


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))