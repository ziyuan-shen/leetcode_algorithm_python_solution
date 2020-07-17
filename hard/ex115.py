class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0
        dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if i == len(s) - 1:
                    if j == len(t) - 1 and s[i] == t[j]:
                        dp[i][j] = 1
                elif s[i] == t[j]:
                    dp[i][j] = (dp[i+1][j+1] if j + 1 < len(t) else 1) + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]
                    