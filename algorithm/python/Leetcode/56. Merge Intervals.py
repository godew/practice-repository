intervals = [[1,4],[0,4]]
intervals.sort()

res = []
s = intervals[0][0]
e = intervals[0][1]
intervals.pop(0)
for interval  in intervals:
    if interval[0] <= e:
        e = max(e, interval[1])
        continue
    res.append([s, e])
    s = interval[0]
    e = interval[1]
res.append([s, e])

print(res)
