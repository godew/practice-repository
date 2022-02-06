from typing import *
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x: (-x[0], x[1]))
        for i in range(1, len(people)):
            people.insert(people[i][1], people[i])
            people.pop(i+1)
        return people
a = Solution()
print(a.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))