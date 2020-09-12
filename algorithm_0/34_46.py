from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        ret = []

        def dfs(elems):
            if not elems:
                result.append(ret[:])
                return
            for elem in elems:
                new_elems = elems[:]
                new_elems.remove(elem)
                ret.append(elem)
                dfs(new_elems)
                ret.pop()
        
        dfs(nums)
        return result

sol = Solution()
nums = [1, 2, 3]
print (sol.permute(nums))