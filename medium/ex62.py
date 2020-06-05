class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[-1][-1] = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i + 1 < n:
                    dp[i][j] += dp[i+1][j]
                if j + 1 < m:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]