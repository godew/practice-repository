import collections
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        count = collections.Counter(nums)
        count = list(count.items())
        count.sort(key= lambda x : -x[1])
        for i in range(k):
            res.append(count[i][0])
            
        return res
