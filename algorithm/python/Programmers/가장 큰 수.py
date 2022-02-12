def solution(numbers):

    numbers = sorted(map(str, numbers), reverse= True)

    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] + numbers[j-1] > numbers[j-1] + numbers[j]:
                numbers[j], numbers[j-1] = numbers[j-1],  numbers[j] # swap
            else:
                break

    return str(int("".join(numbers)))

print(solution([3, 30, 34, 5, 9]))