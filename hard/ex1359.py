from bisect import bisect
class Solution:   
    def countOrders(self, n: int) -> int:
        ans = 1
        for i in range(2, n+1):
            prev_len = (i - 1) * 2
            ans *= (prev_len + 2) * (prev_len + 1) // 2
            ans %= (10 ** 9 + 7)
        return ans