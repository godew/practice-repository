n = int(input())

res = []
# insert sort
# for _ in range(n):
#     tmp = int(input())
#     for i, x in enumerate(res): # insert할 위치 찾기
#         if x >= tmp:
#             res.insert(i, tmp)
#             break
#     else:
#         res.append(tmp)


# bubble sort
for _ in range(n):
    res.append(int(input()))
    
for i in range(n-1, 0, -1):
    for j in range(i):
        if res[j] > res[j+1]:
            res[j], res[j+1] = res[j+1], res[j]

for x in res:
    print(x)

