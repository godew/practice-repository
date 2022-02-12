def solution(word):
    cnt = [0]
    tmp = []
    def DFS(L):
        if tmp == list(word):
            return True
        if L == 5:
            return False
        for ch in ["A", "E", "I", "O", "U"]:
            cnt[0] += 1
            tmp.append(ch)
            if DFS(L + 1):
                return True
            tmp.pop()

    DFS(0)
    return cnt[0]

print(solution("EIO"))