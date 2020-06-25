class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k <= 0:
            return 0
        if k >= len(prices) // 2:
            return sum([i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0])
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for t in range(1, k+1):
            maxval = float("-inf")
            for d in range(1, len(prices)):
                maxval = max(maxval, dp[t-1][d-1] - prices[d-1])
                dp[t][d] = max(maxval + prices[d], dp[t][d-1])
        return dp[-1][-1]