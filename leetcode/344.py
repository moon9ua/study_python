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

'''
* name 'List' is not defined 오류: https://stackoverflow.com/questions/57505071/nameerror-name-list-is-not-defined
    * `from typing import List` 추가로 해결
* 모듈 사용하기: https://dojang.io/mod/page/view.php?id=2441
* typing 모듈로 타입 표시하기: https://www.daleseo.com/python-typing/
* a, b = b, a
'''