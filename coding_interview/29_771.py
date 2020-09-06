# 내 풀이
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         count = 0
#         for s in S:
#             if s in J:
#                 count += 1
#         return count

# 리스트 컴프리헨션
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # return (sum([s in J for s in S])) # 이렇게 해야하는 줄 알았는데, 아래 코드도 된다.
        return (sum(s in J for s in S)) # 아래 코드가 훨씬 빠르다. `s in J for s in S`는 도대체 뭐지? 리스트도 아니고.

sol = Solution()
J = "aA"
S = "aAAbbbb"
print (sol.numJewelsInStones(J, S))