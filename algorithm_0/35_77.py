# 내 답안
# from typing import List
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         nums = list(range(1, n + 1))
#         result = []
#         ret = []

#         def dfs(elems):
#             if len(ret) == k:
#                 result.append(ret[:]) # 이걸 빼먹음!
#                 return
#             for e in elems:
#                 if not ret:
#                     new_elems = elems[elems.index(e):]
#                 else:
#                     new_elems = elems[:] # 중복을 해결을 못함
#                 new_elems.remove(e)
#                 ret.append(e)
#                 dfs(new_elems)
#                 ret.pop()

#         dfs(nums)
#         return (result)

# 책 답안
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            print (elements, start, k) # 공부용
            if k == 0:
                results.append(elements[:])
                # print (f"결과: {elements[:]}")
                return # 안하고 하고 차이를 눈여겨보자.
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

sol = Solution()
n = 3
k = 2
sol.combine(n, k)
print (sol.combine(n, k))