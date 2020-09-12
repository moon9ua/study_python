from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        ret = []
        def dfs(elem, target, index):
            if target == 0:
                result.append(ret[:])
                return
            elif target < 0:
                return
            for index in range(index, len(elem)):
                ret.append(elem[index])
                dfs(elem, target - elem[index], index) # index를 포함시키는 아이디어.
                ret.pop()
        dfs(candidates, target, 0)
        return result

sol = Solution()
candidates = [2,3,5]
target = 8
print (sol.combinationSum(candidates, target))