from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
                
        res = [0]*len(nums)
        res[0] = nums[0]
        res[1] = max(nums[1], res[0])
        for i in range(2, len(nums)):
            res[i] = max(res[i-2]+nums[i], res[i-1])
                         
        return res[-1]
  

a = Solution()
print(a.rob([2,7,9,3,1]))