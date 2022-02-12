def solution(record):
    id = {}
    res = []
    for s in record:
        s = s.split()
        if s[0] == "Enter":
            id[s[1]] = s[2]
            res.append(s[1] + "님이 들어왔습니다.")
        elif s[0] == "Leave":
            res.append(s[1] + "님이 나갔습니다.")
        else:
            id[s[1]] = s[2]

    for i in range(len(res)):
        res[i] = res[i].replace(res[i].split("님")[0], id[res[i].split("님")[0]])
    return res

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

