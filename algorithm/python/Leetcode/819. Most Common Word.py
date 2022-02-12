import re
from typing import List
import collections 

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         tmp = ""
#         paragraph = paragraph.lower()
#         for x in paragraph:
#             if x.isalnum():
#                 tmp += x
#             else:
#                 tmp += " "

#         tmp = tmp.split()

#         MAX = 0
#         for s in tmp:
#             if MAX < tmp.count(s) and s not in banned:
#                 MAX = tmp.count(s)
#                 res = s

#         return res

# 해답 코드

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]