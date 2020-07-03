class Solution:           
    def canPartition(self, nums: List[int]) -> bool:
        cum = sum(nums)
        if cum % 2 == 1:
            return False
        target = cum // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        dp[0][0] = True
        if nums[0] < target + 1:
            dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(target+1):
                if dp[i-1][j]:
                    dp[i][j] = True
                if dp[i-1][j] and j + nums[i] < target + 1:
                    dp[i][j+nums[i]] = True
        return dp[-1][-1]