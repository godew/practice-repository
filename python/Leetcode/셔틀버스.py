def trans(n):
    return str(n).zfill(4)[:2] + ":" + str(n).zfill(4)[2:]

def solution(n, t, m, timetable):
    for i, time in enumerate(timetable):
        timetable[i] = int(time[:2] + time[3:])
    timetable.sort()

    start = 900
    tmp = -1
    idx = 0
    for _ in range(n):
        limit = m
        for i in range(idx, len(timetable)):
            if limit == 0:
                idx = i
                break
            if n == 1 and limit == 1:
                if tmp == -1:
                    if timetable[i] % 100 == 0:
                        return trans(timetable[i]-41)
                    else:
                        if start >= timetable[i]:
                            return trans(timetable[i]-1)
                        else:
                            return trans(start)
                if timetable[i] == tmp:
                    if timetable[i] % 100 == 0:
                        return trans(timetable[i]-41)
                    else:
                        return trans(timetable[i]-1)
                else:
                    return trans(tmp)
            if start >= timetable[i]:
                limit -= 1
            else:
                idx = i
                break
        if n == 1:
            return trans(start)
        start += (t//60)*100 + (t % 60)
        n -= 1