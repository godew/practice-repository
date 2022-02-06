
def solution(bridge_length, weight, truck_weights):
    q = [0]*bridge_length
    t = 0

    i = 0
    while True:
        t += 1
        q.pop(0)
            
        if sum(q) + truck_weights[i] > weight:
            q.append(0)
            continue
        
        q.append(truck_weights[i])
        i += 1

        if i == len(truck_weights):
            t += bridge_length
            break

    return t

print(solution(2, 10, [7,4,5,6]))