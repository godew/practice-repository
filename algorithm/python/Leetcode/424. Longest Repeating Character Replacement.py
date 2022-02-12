import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tmp = collections.Counter({})
        res = 0
        rt = 0
        for i in range(len(s)):
            if len(s)-i <= res:
                break
            if i != 0:
                tmp[s[i-1]] -= 1
            if i != 0 and s[i] == s[i-1]:
                continue
            for j in range(rt, len(s)):
                tmp[s[j]] += 1
                if (j-i+1) - tmp.most_common(1)[0][1] > k:
                    tmp[s[j]] -= 1
                    res = max(res, j-i)
                    rt = j
                    break
            else:
                res = max(res, j-i+1) # 마지막꺼 비교
                break
        return res

a = Solution()
print(a.characterReplacement("ABAB", 2))


