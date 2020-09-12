# # 내 풀이
# from typing import List
# import re
# import collections
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         paragraph = re.sub("[,.]", "", paragraph) # 여기가 틀림. !같은 문장부호를 못거름.
#         para_list = paragraph.lower().split()
#         for banned_word in banned:
#             banned_word = banned_word.lower()
#             para_list.remove(banned_word)
#         counts = collections.Counter(para_list)
#         return counts.most_common(1)[0][0]

# 책 풀이
from typing import List
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned] # 이게 도대체 뭐지?
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

test1 = Solution()
para = "Bob hit a ball, the hit BALL flew far after it was hit."
ban = ["hit"]
print (Solution.mostCommonWord(test1, para, ban))