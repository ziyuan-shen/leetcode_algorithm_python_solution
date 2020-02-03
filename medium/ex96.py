class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            dp[i] = 2 * dp[i-1] + sum([dp[k-1] * dp[i-k-1] for k in range(1, i)])
        return dp[-1]