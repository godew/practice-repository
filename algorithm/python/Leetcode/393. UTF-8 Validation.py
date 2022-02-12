from typing import *
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0 
        for x in data:
            if not cnt: # cnt == 0이면 첫바이트이므로 검증
                if 0 <= x <= 127:
                    continue
                elif 192 <= x <= 223:
                    cnt = 1
                elif 224 <= x <= 239:
                    cnt = 2
                elif 240 <= x <= 247:
                    cnt = 3
                else:
                    return False
            else:

                if 128 <= x <= 191:
                    cnt -= 1
                else:
                    return False
                
        return not cnt