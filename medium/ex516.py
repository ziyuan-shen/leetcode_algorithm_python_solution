class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 1):
            dp[i][i+1] = 2 if s[i] == s[i+1] else 1
        for l in range(2, length):
            for i in range(length - l):
                dp[i][i+l] = max(dp[i+1][i+l-1] + 2 if s[i] == s[i+l] else dp[i+1][i+l-1], dp[i+1][i+l], dp[i][i+l-1])
        return dp[0][length-1]