from typing import *
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 삽입 정렬 스왑을 최소로 하기위해 큰 순서로 정렬한다.
        nums = list(map(str, nums))
        nums.sort(reverse=True)
        res = [] # 정렬된 리스트

        # 삽입 정렬
        for x in nums:
            for i in range(len(res)-1, -1, -1):
                if int(x+res[i]) <= int(res[i]+x):
                    res.insert(i+1, x)
                    break
            else:
                res.insert(0, x)

        return str(int(("".join(res))))





