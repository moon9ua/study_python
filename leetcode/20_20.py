class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop(-1):
                return False
        return len(stack) == 0

# test = []
# print(not test)

sol = Solution()
print(sol.isValid("]"))