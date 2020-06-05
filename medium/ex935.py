from collections import defaultdict
class Solution:
    def knightDialer(self, N: int) -> int:
        dp = [defaultdict(int) for _ in range(N)]
        for i in range(10):
            dp[0][i] = 1
        nextdic = {0: [4, 6], 1:[6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        for i in range(1, N):
            for num in range(10):
                for nextnum in nextdic[num]:
                    dp[i][num] += dp[i-1][nextnum]
        return sum(list(dp[-1].values())) % (10 ** 9 + 7)