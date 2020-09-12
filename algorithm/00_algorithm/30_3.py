# # 내 풀이 # 반복문이 두번 중첩되니 당연히 엄청 느림.
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#         ret = [0] * len(s)
#         for i in range(len(s)):
#             lst = []
#             for mover in s[i:]:
#                 if mover not in lst:
#                     lst.append(mover)
#                     ret[i] += 1
#                 else:
#                     break
#         return max(ret)

# sol = Solution()
# s = "czswbbcfrwmvbykvgnfcavtnatgyqtuusnsvovahtpf"
# print (sol.lengthOfLongestSubstring(s))

# 책 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 # start가 왼쪽 포인터
        ret = 0
        used = {}
        for i, char in enumerate(s): # i가 오른쪽 포인터
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                ret = max(ret, i - start + 1)
            used[char] = i
        return ret

sol = Solution()
s = "czswbbcfrwmvbykvgnfcavtnatgyqtuusnsvovahtpf"
print (sol.lengthOfLongestSubstring(s))