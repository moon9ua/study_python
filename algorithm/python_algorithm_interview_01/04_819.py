# ---
from typing import List
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [x for x in re.sub(r"[^\w]", " ", paragraph).lower().split()
                    if x not in banned] # r은 뭐지? # 리스트 컴프리헨션
        print (words)
        count = collections.Counter(words)
        return count.most_common(1)[0][0]

# ---
sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print (sol.mostCommonWord(paragraph, banned))