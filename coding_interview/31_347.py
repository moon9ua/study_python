import collections
from typing import List

# 내 풀이
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = collections.Counter(nums)
#         ret = []
#         for elem in counter.most_common(k):
#             ret.append(elem[0])
#         return (ret)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        ret = list(zip(*counter.most_common(k)))[0]
        return (ret)

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))