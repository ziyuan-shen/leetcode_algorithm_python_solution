class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            return s==s[::-1]
        
        if isPalindrome(s):
            return True
        else:
            idx = 0
            length = len(s)
            while idx<length and (s[idx] == s[-1-idx]):
                idx +=1
            return isPalindrome(s[:idx]+s[idx+1:]) or isPalindrome(s[:length-1-idx]+s[length-idx:])