from typing import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        tmp = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        if sum(diff) < 0:
            return -1
        
        for i in range(len(diff)):
            if i in tmp:
                continue
            if diff[i] < 0:
                continue
            w = 0
            for j in range(i, len(diff)+i): # 순환이므로 len(diff)길이만큼 반복
                w += diff[j%len(diff)] # 모듈러 연산으로 순환시킨다
                if diff[j%len(diff)] >= 0:
                    tmp.append(j%len(diff))
                if w < 0:

                    break
            else:
                return i # 답은 유일하다.
            

a = Solution()
print(a.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))