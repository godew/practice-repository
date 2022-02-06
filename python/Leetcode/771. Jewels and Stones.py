import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        count = collections.Counter(stones)
        
        for ch in jewels:
            # Counter객체는 존재하지 않는 키의 경우 KeyError가 아니라 0을 출력해준다.
            # if ch in count:
            #     res += count[ch]
            res += count[ch]

        return res