class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        mini = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            mini = min(mini, prices[i])
            if prices[i] - mini > 0:
                ans = max(ans, prices[i] - mini + self.maxProfit(prices[i+2:]))
        return ans