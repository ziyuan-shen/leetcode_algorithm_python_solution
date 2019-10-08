class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        copy = l.copy()
        l.reverse()
        return l == copy