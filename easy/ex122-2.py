class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        idx = 0
        while idx < len(prices):
            while idx + 1 < len(prices) and prices[idx+1] <= prices[idx]:
                idx += 1
            if idx < len(prices):
                valley = prices[idx]
                idx += 1
                while idx + 1 < len(prices) and prices[idx+1] >= prices[idx]:
                    idx += 1
                if idx < len(prices):
                    peek = prices[idx]
                    ans += (peek - valley)
                    idx += 1
        return ans