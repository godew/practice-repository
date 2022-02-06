
def solution(numbers, target):
    res = []

    def DFS(L, tot):
        if L == len(numbers):
            if tot == target:
                res.append(0)
            return
        
        DFS(L+1, tot + numbers[L])
        DFS(L+1, tot - numbers[L])

    DFS(0, 0)
    return len(res)
print(solution([1, 1, 1, 1, 1], 3))