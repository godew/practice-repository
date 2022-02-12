def hanoi(n, start, end):
    if n == 1:
        res.append([start, end])
        return
    
    hanoi(n-1, start, 6-start-end)
    res.append([start, end])
    hanoi(n-1, 6-start-end, end)
    
def solution(n):
    global res
    res = []
    hanoi(n, 1, 3)

    return res

print(solution(2))

