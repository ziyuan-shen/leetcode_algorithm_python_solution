class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        for idx in range(len(s)-1, -1, -1):
            if s[:idx+1] == s[idx::-1]:
                return s[-1:idx:-1] + s