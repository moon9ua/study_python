import collections
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = collections.deque()
        for char in s:
            if char.isalnum():
                new_s.append(char.lower())
        while len(new_s) > 1:
            if new_s.pop() != new_s.popleft():
                return False
        return True

sol = Solution()
s = "A man, a plan, a canal: Panama"
# s = "race a car"
print (sol.isPalindrome(s))