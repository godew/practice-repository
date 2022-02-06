class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        len_max = 0
        for ch in s:
            if ch in res:
                res = res[res.index(ch)+1:]
            res.append(ch)
            len_max = max(len_max, len(res))

        return len_max