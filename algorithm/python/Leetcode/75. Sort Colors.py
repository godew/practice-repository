import collections 
from typing import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = collections.Counter(nums)
        res = []
        if 0 in tmp.keys():
            res += [0]*(tmp[0])
        if 1 in tmp.keys():
            res += [1]*(tmp[1])
        if 2 in tmp.keys():
            res += [2]*(tmp[2])
        
        for i in range(len(nums)):
            nums[i] = res[i]
        
        