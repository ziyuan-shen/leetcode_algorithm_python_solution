from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        squares = [num ** 2 for num in range(1, int(n ** 0.5) + 1)]
        for i in range(1, n+1):
            ans = float("inf")
            for square in squares:
                if square <= i:
                    ans = min(ans, dp[i-square] + 1)
            dp[i] = ans
        return dp[-1]