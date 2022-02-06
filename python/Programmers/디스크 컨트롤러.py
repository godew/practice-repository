import heapq
def solution(jobs):
    heap = []
    res = 0
    jobs.sort()

    i = 0
    limit = 0
    while i < len(jobs):
        if limit < jobs[i][0]:
            if not heap:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
                limit = jobs[i][0]
                i += 1
            job = heapq.heappop(heap)
            res += limit + job[0] - job[1]
            limit += job[0]
            continue

        heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
        i += 1

    while heap:
        job = heapq.heappop(heap)
        res += limit + job[0] - job[1]
        limit += job[0]

    return res // len(jobs)

print(solution([[0, 3], [2, 6], [1, 9]]))