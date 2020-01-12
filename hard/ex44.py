class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[-1] = [p[j:] == (len(p) - j) * "*" for j in range(len(p) + 1)]
        for i in range(len(s) - 1, -1 , -1):
            for j in range(len(p) - 1, -1, -1):
                if p[j] == "?":
                    dp[i][j] = dp[i+1][j+1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]
                else:
                    dp[i][j] = s[i] == p[j] and dp[i+1][j+1]
        return dp[0][0]