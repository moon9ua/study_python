import collections

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
        
s = "bcda"
test = set(s)
print (test)
counter = collections.Counter(s)
print (counter)