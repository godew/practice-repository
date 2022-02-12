def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i+1:
            break
    else:
        return i+1
    return i



print(solution([10,11,12,13,14]))