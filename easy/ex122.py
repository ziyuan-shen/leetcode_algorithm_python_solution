class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        valley_idx = 0
        peak_idx = 1
        profit = 0
        while valley_idx < len(prices) - 1:
            while (valley_idx+1) < (len(prices)-1) and prices[valley_idx] > prices[valley_idx+1]:
                valley_idx += 1
            peak_idx = valley_idx + 1
            while (peak_idx+1) < len(prices) and prices[peak_idx+1] > prices[peak_idx]:
                peak_idx += 1
            if prices[peak_idx] > prices[valley_idx]:
                profit += prices[peak_idx] - prices[valley_idx]
            valley_idx = peak_idx + 1
        return profit