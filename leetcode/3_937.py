# # 내 풀이
# from typing import List
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         char = []
#         num = []
#         for log in logs:
#             tmp = log.split(" ")
#             if tmp[1].isnumeric():
#                 num.append(log)
#             else:
#                 char.append(log)
#         char.sort() # 이 부분을 해결 못함
#         return char + num

# 공부
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        char, num = [], [] # 한 줄로 가능
        for log in logs:
            tmp = log.split(" ")
            if tmp[1].isnumeric():
                num.append(log)
            else:
                char.append(log)
        # for i in char:
        #     test = lambda x: (x.split(" ")[1:], x.split(" ")[0])
        #     print (test(i), type(test(i))) # 람다 이해를 위한 테스트 내용
        char.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return char + num

test1 = Solution()
test2 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print (Solution.reorderLogFiles(test1, test2))