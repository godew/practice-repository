import math
def solution(brown, yellow):
    a = 1
    b = - (2 + brown // 2)
    c = brown + yellow
    x = (int)(-b + math.sqrt(b**2 - 4*a*c)) // 2 * a
    y = (int)(-b - math.sqrt(b**2 - 4*a*c)) // 2 * a

    return [x, y]

print(solution(8, 1))