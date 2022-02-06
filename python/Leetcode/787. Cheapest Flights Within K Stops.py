
import collections
n = 4; flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]; src = 0; dst = 3; k = 1
node_val = [0]*n
q = collections.deque()
tmp = collections.defaultdict(list)
for x in flights:
    tmp[x[0]].append([x[1], x[2]])

q.append(src)
for _ in range(k+1):
    if not q:
        break
    node_val_tmp = [0]*n
    node = set()
    while q:
        new = q.popleft()
        for x in tmp[new]:
            node.add(x[0])
            if node_val_tmp[x[0]] == 0:
                node_val_tmp[x[0]] = node_val[new]+x[1]
            elif node_val_tmp[x[0]] > node_val[new]+x[1]:
                node_val_tmp[x[0]] = node_val[new]+x[1]
    for x in node:
        q.append(x)
        if node_val[x] == 0:
            node_val[x] = node_val_tmp[x]
        else:
            node_val[x] = min(node_val_tmp[x], node_val[x])

if node_val[dst] == 0:
    print(-1)
else:
    print(node_val[dst])

    




