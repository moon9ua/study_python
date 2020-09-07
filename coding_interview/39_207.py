import collections
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


sol = Solution()
numCourses = 2
# prerequisites = [[1,0]]
prerequisites = [[1,0],[0,1]]
print (sol.canFinish(numCourses, prerequisites))

