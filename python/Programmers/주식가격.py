def solution(prices):
    res = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                res.append(cnt)
                break
        else:
            res.append(cnt)

    return res

print(solution([1, 2, 3, 2, 3]))