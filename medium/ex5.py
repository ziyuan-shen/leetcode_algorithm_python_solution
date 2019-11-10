class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length==0:
            return ''
        DP = [[False]*i for i in range(length, 0, -1)]
        max_substring = s[0]
        for i in range(length):
            DP[i][0] = True
        for i in range(length-1):
            DP[i][1] = (s[i]==s[i+1])
            if DP[i][1]:
                max_substring = s[i:i+2]
        for i in range(2, length):
            for j in range(0, length-i):
                DP[j][i] = (s[j] == s[i+j]) and DP[j+1][i-2]
                if DP[j][i]:
                    max_substring = s[j:j+i+1]
        return max_substring