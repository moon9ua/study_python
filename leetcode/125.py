# https://leetcode.com/problems/valid-palindrome/

# 풀이0 - 리스트 (52ms)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         pure = []
#         for c in s:
#             if c.isalnum():
#                 pure.append(c.lower())
#         rev = pure[::-1]
#         # if pure == rev:
#         #     return True
#         # else:
#         #     return False
#         return pure == rev # 위 네 줄을 한 줄로.

# 풀이1 - 문자열, 정규표현식 (36ms)
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub("[^a-z0-9]", "", s) # re.sub()
#         rev = s[::-1]
#         return s == rev

# 풀이2 - 문자열 (40ms)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pure = ""
        for c in s:
            if c.isalnum():
                pure += c
        rev = pure[::-1]
        return pure == rev

# 클래스의 함수 사용
a = Solution()
print(Solution.isPalindrome(a, "0P")) # 언바운드 메서드

'''
* [ ] 클래스에 대해 공부 필요
    * 함수 사용법부터 헤맸음
    * 언바운드 메서드
* 문자열 필터링
    * re.sub()
    * 정규표현식
'''