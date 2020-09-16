# ---
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        word = []
        digit = []
        for log in logs:
            splited = log.split()
            # if (splited[1].isnumeric()):
            if (splited[1].isdigit()): # isdigit()?
                digit.append(log)
            else:
                word.append(log)
        word.sort(key= lambda x: (x.split()[1:], x.split()[0]))
        return word + digit

# ---
sol = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print (sol.reorderLogFiles(logs))