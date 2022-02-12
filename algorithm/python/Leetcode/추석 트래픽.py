def solution(lines):
    res = 0
    bars = []
    for line in lines:
        rt = int(line[11:13]) * 3600 + int(line[14:16]) * 60 + float(line[17:23])
        lt = round(rt - float(line[24:-1]) + 0.001, 3) # 소수점 셋째 자리까지
        bars.append([lt,rt])

    for i in range(len(bars)):
        lt = bars[i][1]
        rt = round(lt + 1 - 0.001, 3)
        cnt = 1
        for j in range(i+1, len(bars)):
            if not (bars[j][1] < lt or bars[j][0] > rt ): # 1초 범위에 포함되면
                cnt += 1
        res = max(res, cnt)

    return res
    
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))