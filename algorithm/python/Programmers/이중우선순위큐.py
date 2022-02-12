import heapq
def solution(operations):
    heap = []
    for operation in operations:
        operation = operation.split()
        if operation[0] == "I":
            heapq.heappush(heap, int(operation[1]))
        elif operation[1] == "1" and heap:
            heap = list(map(lambda x : -x, heap))
            heapq.heapify(heap)
            heapq.heappop(heap)
            heap = list(map(lambda x : -x, heap))
            heapq.heapify(heap)
        elif operation[1] == "-1" and heap:
            heapq.heappop(heap)

    if heap:
        return [max(heap), min(heap)]
    else:
        return [0,0]


print(solution(["I 7","I 5","I -5","D -1"]	))