from typing import *
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        tot = 0
        for x in nums:
            tot += x
            res = max(res, tot)
            if tot < 0:
                tot = 0
        return res

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))