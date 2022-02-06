def solution(number, k):
    tmp = []
    cnt = 0

    for idx, n in enumerate(number):
        if not tmp:
            tmp.append(n)
        else:
            while tmp:
                if tmp[-1] < n: # 사전식 비교 "1" < "2"
                    tmp.pop()
                    cnt += 1
                    if cnt == k:
                        return "".join(tmp) + number[idx:]
                else:
                    tmp.append(n)
                    break
            else:
                tmp.append(n)
    else: # 지울게 없다 ex) 444444
        return "".join(tmp[:len(tmp) - (k - cnt)])
        

print(solution("444444", 4))


