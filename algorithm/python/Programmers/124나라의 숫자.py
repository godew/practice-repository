def solution(n):
    res = ""
    while n:
        if n % 3 == 0:
            res += "4"
            n = (n - 3) // 3
        else:
            res += str(n % 3)
            n //= 3

    return res[::-1]
    
print(solution(10))