class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left_profits = [0 for _ in range(len(prices))]
        right_profits = [0 for _ in range(len(prices))]
        left_min = prices[0]
        right_max = prices[-1]
        for i in range(1, len(prices)):
            left_profits[i] = max(left_profits[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])
        for i in range(len(prices) - 2, -1, -1):
            right_profits[i] = max(right_profits[i+1], right_max - prices[i])
            right_max = max(right_max, prices[i])
        right_profits.append(0)
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, left_profits[i]+right_profits[i+1])
        return ans