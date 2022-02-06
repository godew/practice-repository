import collections

def solution(str1, str2):

    mul_1 = collections.Counter(makeMul(str1))
    mul_2 = collections.Counter(makeMul(str2))
     
    # intersection / union
    if len(list((mul_1|mul_2).elements())):
        res = len(list((mul_1&mul_2).elements())) / len(list((mul_1|mul_2).elements())) 
    else:
        return 65536

    return int(res*65536)

def makeMul(a):
    mul = []
    for i in range(len(a)-1):
        tmp = a[i:i+2]
        for c in tmp:
            if not c.isalpha():
                break
        else:
            mul.append(tmp.lower())
        
    return mul