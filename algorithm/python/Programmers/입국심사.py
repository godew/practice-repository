def solution(n, times):
    times.sort()
    ch = [0]*len(times)
    for i in range(n):
        if not ch.count(0):# 꽉차거나 기다리면
            tmp = min(ch)
            ch = list(map(lambda x : x - tmp if x - tmp >= 0 else 0, ch))
            ch.index(min(ch))
        idx = ch.index(0) # 가장 왼쪽에 비어있는 곳
        ch[idx] = times[idx]
        


print(solution(6, [7, 10]))