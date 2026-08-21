class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                word = s[i:j+1]

                if word == word[::-1] and len(word) > len(ans):
                    ans = word
        return ans
        