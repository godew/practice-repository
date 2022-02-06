from itertools import combinations

def solution(line):
    # 좌표 구하기
    coordinate = []
    for l1, l2 in combinations(line, 2):
        tmp = l1[0]*l2[1] - l1[1]*l2[0]
        if tmp == 0:
            continue
        x = (l1[1]*l2[2] - l1[2]*l2[1]) / tmp
        y = (l1[2]*l2[0] - l1[0]*l2[2]) / tmp
        if x.is_integer() and y.is_integer():
            coordinate.append([int(x), int(y)])
    
    # 그림그리기
    left = min(coordinate, key= lambda x : x[0])[0]
    right = max(coordinate, key= lambda x : x[0])[0]
    bottom = min(coordinate, key= lambda x : x[1])[1]
    top = max(coordinate, key= lambda x : x[1])[1]
    res = [["."] * (right - left + 1) for _ in range(top - bottom + 1)]
    for x, y in coordinate:
        res[top - y][x - left] = "*"
    
    return ["".join(s) for s in res]

print(solution([[100000, -100000, 100000], [-100000, -100000, 100000], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))