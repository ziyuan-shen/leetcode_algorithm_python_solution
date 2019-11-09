class Solution:
    def isPalindrome(self, s):
        idx = 0
        while idx < len(s) // 2:
            if s[idx] != s[-1-idx]:
                return False
            idx += 1
        return True
        
    def longestPalindrome(self, s: str) -> str:
        max_length = len(s)
        while max_length>0:
            for i in range(len(s)-max_length+1):
                substring = s[i:i+max_length]
                if self.isPalindrome(substring):
                    return substring
            max_length -= 1
        return ''