from collections import Counter
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(len(nums))] for _ in range(3)]
        dp[nums[0] % 3][0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] % 3 == 0:
                dp[0][i] = dp[0][i-1] + nums[i]
                dp[1][i] = dp[1][i-1] + nums[i] if dp[1][i-1] else 0
                dp[2][i] = dp[2][i-1] + nums[i] if dp[2][i-1] else 0
            if nums[i] % 3 == 1:
                dp[0][i] = max(dp[2][i-1] + nums[i] if dp[2][i-1] else 0, dp[0][i-1])
                dp[1][i] = max(dp[0][i-1] + nums[i], dp[1][i-1])
                dp[2][i] = max(dp[1][i-1] + nums[i] if dp[1][i-1] else 0, dp[2][i-1])
            if nums[i] % 3 == 2:
                dp[0][i] = max(dp[1][i-1] + nums[i] if dp[1][i-1] else 0, dp[0][i-1])
                dp[1][i] = max(dp[2][i-1] + nums[i] if dp[2][i-1] else 0, dp[1][i-1])
                dp[2][i] = max(dp[0][i-1] + nums[i], dp[2][i-1])
        print(dp)
        return dp[0][-1]