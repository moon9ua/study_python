# ---
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_log = []
        int_log = [] # 다중할당으로 한줄로 줄일 수.
        for log in logs:
            if log.split()[1].isalpha():
                str_log.append(log)
            else:
                int_log.append(log)
        
        str_log.sort(key = lambda x: (x.split()[1:], x.split()[0])) # 람다식

        return str_log + int_log

# ---
sol = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print (sol.reorderLogFiles(logs))