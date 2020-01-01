class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        mincoin = min(coins)
        dp = [0] * amount
        for i in range(1, amount+1):
            if i < mincoin:
                dp[i-1] = -1
            elif i in coins:
                dp[i-1] = 1
            else:
                dp[i-1] = min([dp[i-coin-1] + 1 if (i-coin) > 0 and dp[i-coin-1] != -1 else float("Inf") for coin in coins])
                if dp[i-1] == float("Inf"):
                    dp[i-1] = -1
        return dp[-1]