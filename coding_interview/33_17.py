from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
                "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        # 책 답안
        # def dfs(index, path):
        #     if len(path) == len(digits):
        #         result.append(path)
        #         return
        #     for i in range(index, len(digits)): # 이 줄이 이해가 안됨...
        #         for j in dic[digits[i]]:
        #             print (i, j)
        #             dfs(i + 1, path + j)
        # if not digits:
        #     return []
        # result = []
        # dfs(0, "")
        # return result

        # 내 답안
        def dfs(i, ret):
            if len(ret) == len(digits):
                result.append(ret)
                return
            for char in dic[digits[i]]:
                dfs(i + 1, ret + char)
        if not digits:
            return []
        result = []
        dfs(0, "")
        return result

sol = Solution()
digits = "235"
print (sol.letterCombinations(digits))
