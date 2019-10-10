class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_str = ''
        for i in s:
            if i.isalnum():
                alnum_str += i
        alnum_str = alnum_str.lower()
        if alnum_str[::-1] == alnum_str:
            return True
        else:
            return False