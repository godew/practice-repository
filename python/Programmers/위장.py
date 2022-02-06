import collections
def solution(clothes):
    tmp = collections.defaultdict(list)
    res = 1
    for cloth, kind in clothes:
        tmp[kind].append(cloth)
    for v in tmp.values():
        res *= len(v) + 1
    return res - 1
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))