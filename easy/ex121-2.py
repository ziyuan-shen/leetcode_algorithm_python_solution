class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue = prices[0]
        ans = 0
        for price in prices[1:]:
            minvalue = min(minvalue, price)
            ans = max(ans, price - minvalue)
        return ans