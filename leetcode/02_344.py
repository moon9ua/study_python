# 내 풀이
# from typing import List
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         leng = len(s)
#         for i in range(leng // 2):
#             tmp = s[i]
#             s[i] = s[leng - i - 1]
#             s[leng - i - 1] = tmp

# 풀이 2) 파이썬다운 방식
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

test = Solution()
list = ["h","e","l","l","o"]
Solution.reverseString(test, list)
print (list)