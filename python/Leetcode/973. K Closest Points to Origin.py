
points = [[3,3],[5,-1],[-2,4]]; k = 2
tmp = []
res = []
for x, y in points:
    tmp.append([x, y, x ** 2 + y ** 2])

tmp.sort(key= lambda x: x[2])

for i in range(k):
    res.append([tmp[i][0], tmp[i][1]])

print(res)



