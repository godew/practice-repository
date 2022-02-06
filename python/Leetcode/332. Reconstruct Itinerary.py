import collections
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def DFS(s):
            if res:
                return
            
            if len(tmp) == ticket_len:
                res.append(tmp[:])

            for i, ticket in enumerate(tickets):
                fr = ticket[0]
                to = ticket[1]
                if fr == s:
                    tickets.pop(i)
                    tmp.append(to)
                    DFS(to)
                    tickets.insert(i, [s, to])
                    tmp.pop()

        tickets.sort(key= lambda x: x[1])
        ticket_len = len(tickets)+1
        tmp = ["JFK"]
        res = []
        DFS("JFK")

        return res[-1]


tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
graph = collections.defaultdict(list)

for a, b in sorted(tickets):
    graph[a].append(b)
route = []

def dfs(a):
    # 첫 번째 값을 읽어 어휘순 방문
    
    while graph[a]:
        dfs(graph[a].pop(0))
    route.append(a)
    print(route)

dfs('JFK')
print(route)
# # 다시 뒤집어 어휘순 결과로
# print(route[::-1])
