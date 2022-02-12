prices = [1,2]
res = 0
stock = []
for idx, x in enumerate(prices):
    stock.append((x, idx))

stock.sort()
k = 0
for i in range(len(prices)):
    if i > 0 and stock[i][0] == stock[i-1][0]:
        continue
    if res > stock[-1][0] - stock[i][0]:
        break
    for j in range(len(prices)-1,k,-1):
        if stock[i][1] < stock[j][1]:
            if res < stock[j][0] - stock[i][0]:
                res = stock[j][0] - stock[i][0]
                k = j
            break

print(res)