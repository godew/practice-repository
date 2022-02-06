from collections import Counter
def rule(begin, word):
    # 알파벳 한개가 다르면
    return len(list((Counter(begin)&Counter(word)).elements())) == len(begin) - 1


def solution(begin, target, words):
    if target not in words:
        return 0
    ch = [0] * len(words)
    res = [51] # min값, 중첩 함수에서 접근을 위해 배열로 정의
    def DFS(begin, cnt):
        if res[0] <= cnt:
            return
        if begin == target:
            res[0] = cnt
            return
        for i, word in enumerate(words):
            if ch[i] == 0 and rule(begin, word):
                ch[i] = 1
                DFS(word, cnt + 1)
                ch[i] = 0

    DFS(begin, 0)
    return res[0]

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))