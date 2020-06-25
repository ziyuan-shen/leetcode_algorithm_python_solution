class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        mid = len(palindrome) // 2
        for i in range(len(palindrome)):
            if not (i == mid and len(palindrome) % 2 != 0):
                if palindrome[i] != "a":
                    return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"