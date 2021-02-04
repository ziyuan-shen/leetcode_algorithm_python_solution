class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = [0 for _ in range(len(prices))]
        hold = [0 for _ in range(len(prices))]
        hold[0] = - prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i-1], hold[i-1] + prices[i] - fee)
            hold[i] = max(hold[i-1], sell[i-1] - prices[i])
        return sell[-1]