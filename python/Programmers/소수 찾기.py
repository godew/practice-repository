def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1/2))+1 ):
        if n % i == 0:
            return False
    else:
        return True

def DFS(ch, numbers, res, num):
    if sum(ch) == len(numbers):
        return res
    for i, number in enumerate(numbers):
        if ch[i] == 1:
            continue
        ch[i] = 1
        num += number
        if is_prime(int(num)):
            res.add(int(num))
        res = DFS(ch, numbers, res, num)
        num = str(int(num) // 10)
        ch[i] = 0
    return res
    
def solution(numbers):
    ch = [0] * len(numbers)
    res = set()
    return len(DFS(ch, numbers, res, ""))

print(solution("100000"))