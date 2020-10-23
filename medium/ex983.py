class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        next7 = [0 for _ in range(len(days))]
        next30 = [0 for _ in range(len(days))]
        next7[-1] = len(days)
        next30[-1] = len(days)
        idx7 = len(days) - 1
        idx30 = len(days) - 1
        threshold7 = days[-1] - 7
        threshold30 = days[-1] - 30
        for i in range(len(days) - 2, -1, -1):
            if days[i] <= threshold7:
                while days[i] <= threshold7:
                    idx7 -= 1
                    threshold7 = days[idx7] - 7
                idx7 += 1
                next7[i] = idx7
                threshold7 = days[idx7] - 7
            else:
                next7[i] = idx7 + 1
            if days[i] <= threshold30:
                while days[i] <= threshold30:
                    idx30 -= 1
                    threshold30 = days[idx30] - 30
                idx30 += 1
                next30[i] = idx30
                threshold30 = days[idx30] - 30
            else:
                next30[i] = idx30 + 1
        dp = [0 for _ in range(len(days))]
        dp[-1] = min(costs)
        for i in range(len(days) - 2, -1, -1):
            dp[i] = min(costs[0] + dp[i+1], costs[1] + (dp[next7[i]] if next7[i] != len(days) else 0), costs[2] + (dp[next30[i]] if next30[i] != len(days) else 0))
        return dp[0]