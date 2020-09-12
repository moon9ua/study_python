# from typing import List
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         ret = set()

import bisect
nums1 = [1,3,2,4]
nums2 = [2,4]
n1 = 2
i1 = bisect.bisect_right(nums2, n1)
i2 = bisect.bisect_left(nums2, n1)
print (i1)
print (i2)

# https://folivora.tistory.com/83