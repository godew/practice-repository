import collections
import sys

def DFS(k):
    if k in sol_node:
        return
    if k in tmp:
        print(False)
        sys.exit(0)
    
    tmp.append(k)
    for x in graph[k]:
        DFS(x)
    sol_node.append(k)

prerequisites = [[1,0],[0,1]]
graph = collections.defaultdict(list)
sol_node = []
for x, y in prerequisites:
    graph[x].append(y)

for k in list(graph):
    tmp = []
    DFS(k)

print(True)
    


