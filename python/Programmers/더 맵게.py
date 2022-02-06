import heapq
def solution(scoville, K):
    res = 0
    heapq.heapify(scoville)
    while True:
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            return res
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_1 + min_2 * 2)
        res += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1


    
print(solution([1, 2, 3, 9, 10, 12], 7))