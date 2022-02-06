def process(array, command):
    return sorted(array[command[0]-1:command[1]])[command[2]-1]

def solution(array, commands):
    res = []
    for command in commands:
        res.append(process(array, command))

    return res
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))