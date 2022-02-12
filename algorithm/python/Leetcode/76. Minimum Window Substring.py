
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmp = list(t)[:]
        lt = 0
        rt = 0
        res = ""
        while rt <= len(s):
            if not tmp:
                if s[lt] in t and s[lt+1:rt].count(s[lt]) < t.count(s[lt]):
                    if not res:
                        res = s[lt:rt]
                    else:
                        res = min(res, s[lt:rt], key= lambda x: len(x))
                    tmp.append(s[lt])
                lt += 1
            else:
                if rt == len(s):
                    break
                if s[rt] in tmp:
                    tmp.remove(s[rt])
                rt += 1
        return res

a = Solution()
print(a.minWindow("ADOBECODEBANC", "ABC"))

