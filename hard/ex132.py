class Solution:
    def minCut(self, s: str) -> int:
        ispal = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            ispal[i][i] = True
        for i in range(len(s) - 1):
            ispal[i][i+1] = (s[i] == s[i+1])
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                ispal[i][i+length-1] = (s[i] == s[i+length-1]) and ispal[i+1][i+length-2]
        dp = [float("inf") for _ in range(len(s))]
        dp[-1] = 0
        for i in range(len(s) - 2, -1, -1):
            if ispal[i][len(s) - 1]:
                dp[i] = 0
            else:
                for j in range(i, len(s) - 1):
                    if ispal[i][j]:
                        dp[i] = min(dp[i], 1 + dp[j+1])
        return dp[0]