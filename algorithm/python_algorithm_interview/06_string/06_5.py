# ---
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right): # 윈도우 확장
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]: # 풀이는 right - 1이 실제 right임. 나는 right이 실제 right으로 품.
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(0, len(s) - 1):
            result = max(result, expand(i, i), expand(i, i + 1), key=len)
                # 처음에는 expand(i, i + 1), expand(i, i + 2)로 했었는데, expand(i, i), expnad(i, i + 1)로 수정함.
                # 이유는 길이 1인 것을 검사를 안하면 "abcd"와 같은 문자열은 답이 "b"로 제출되기 때문.
                # (복수답안 인정이라 틀린 풀이는 아님. 왜 답이 "b"로 리턴되는지는 직접 반복문을 따라가다 보면 안다.)
                # 따라서 길이가 1인 것도 검사해서, "abcd"와 같은 문자열은 답이 "a"가 제출되게 수정함.

        return result

# ---
# range, 문자열 len(), 문자열 슬라이싱 헷갈리는 것들.
word = "hello"
print (list(range(0, len(word)))) # [0,1,2,3,4] # range의 end는 제외되기 때문.
print ("len(word) =", len(word)) # 5 # 따라서 문자열의 마지막 인덱싱은 len(word) - 1.
print ("word[0:3] =", word[0:3]) # hel # 슬라이싱도 마찬가지로 end는 제외.
print ("word[3:5] =", word[3:5])
# 정리하자면, range나 슬라이싱은 end가 포함이 안됨.
# range나 슬라이싱에서 문자열의 마지막을 나타내려면 len(string). 인덱싱에서 문자열의 마지막을 나타내려면 len(string) - 1.

# ---
sol = Solution()
s1 = "babad"
s2 = "abcde"
print (sol.longestPalindrome(s1))
print (sol.longestPalindrome(s2))