# 책 풀이
from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list) # list가 뭐지?
        for word in strs:
            dict[''.join(sorted(word))].append(word)
        return dict.values()

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
sol.groupAnagrams(strs)
