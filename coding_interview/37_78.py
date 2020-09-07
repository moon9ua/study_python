from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index, path):
            print (f"index:{index}, path:{path}")
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return result

sol = Solution()
nums = [1,2,3]
print (sol.subsets(nums))