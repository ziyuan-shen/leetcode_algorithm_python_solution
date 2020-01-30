class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 1:
            return [0]
        dp = [i for i in range(len(T))]
        for i in range(len(T) - 2, -1, -1):
            warmer_day_idx = i + 1
            while T[warmer_day_idx] <= T[i]:
                next_warmer_day_idx = dp[warmer_day_idx]
                if next_warmer_day_idx == warmer_day_idx:
                    break
                else:
                    warmer_day_idx = next_warmer_day_idx
            if T[warmer_day_idx] > T[i]:
                dp[i] = warmer_day_idx
            else:
                dp[i] = i
        return [dp[i] - i for i in range(len(dp))]