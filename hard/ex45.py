class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [float("inf") for _ in range(len(nums))]
        dp[-1] = 0
        if nums[-2] >= 1:
            dp[-2] = 1
        for i in range(len(dp)-2, -1, -1):
            if nums[i] > 0:
                dp[i] = 1 + min(dp[i+1:min(i+nums[i]+1, len(dp))])
        return dp[0]