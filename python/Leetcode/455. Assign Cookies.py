from typing import *
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)

        tmp = 0
        res = 0
        for i in range(len(s)):
            for j in range(tmp, len(g)):
                if s[i] >= g[j]:
                    res += 1
                    tmp = j+1
                    break
            else:
                break
        return res    


a = Solution()
print(a.findContentChildren([1,2,3], [1,1]))