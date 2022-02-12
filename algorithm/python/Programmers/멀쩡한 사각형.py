import math

def solution(w,h):
    gcd = math.gcd(w,h)
    if gcd == 1:
        res = w + h - 1
    else:
        res = gcd * (w // gcd + h // gcd - 1) # 결국 w + h - 1
    
    return w * h - res
    
print(solution(8, 12))