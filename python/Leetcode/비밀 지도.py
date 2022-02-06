def solution(n, arr1, arr2):

    answer = []
    for i in range(n):
        answer.append("")
        for j in range(n):
            if not(arr1[i] % 2) and not(arr2[i] % 2):
                answer[-1] += " "
            else:
                answer[-1] += "#"
            arr1[i] //= 2
            arr2[i] //= 2
        answer[-1] = answer[-1][::-1]

    return answer