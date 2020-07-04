class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        ans = 1
        idx = len(self.prices) - 2
        while idx >= 0:
            if self.prices[idx] <= price:
                ans += self.spans[idx]
                idx -= self.spans[idx]
            else:
                break
        self.spans.append(ans)
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)