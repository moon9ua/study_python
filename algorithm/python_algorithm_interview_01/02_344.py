# ---
# 풀이1: 파이썬다운 방식. 리트코드에서는 안됨.
# (Wrong Answer)

# from typing import List
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s = s[::-1]

# ---
# 풀이1 수정: 정확히 위와 뭐가 다른지 모르겠음.
# (212ms, 18.5MB)

# from typing import List
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s[:] = s[::-1] # 참조가 아닌 복사를 수행하는 건가?

# ---
# 풀이2: 전통적인 풀이...이지만 파이썬이라 임시변수에 담지 않아도 된다.
# (204ms, 18.5MB)

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

# ---
sol = Solution()
s = ["h","e","l","l","o"]
print (sol.reverseString(s))