class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [0 for _ in range(len(prices))]
        dp2 = [0 for _ in range(len(prices))]
        minvalue = prices[0]
        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i-1], prices[i] - minvalue)
            minvalue = min(minvalue, prices[i])
        maxvalue = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            dp2[i] = max(dp2[i+1], maxvalue - prices[i])
            maxvalue = max(maxvalue, prices[i])
        ans = 0
        for i in range(1, len(prices) - 1):
            ans = max(ans, dp1[i] + dp2[i+1])
        ans = max(dp1[-1], ans, dp2[0])
        return ans