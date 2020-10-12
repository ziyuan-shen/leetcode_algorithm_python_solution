class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [[] for _ in range(len(nums))]
        dp[0] = [nums[0]]
        ans = [nums[0]]
        for i in range(1, len(nums)):
            subset = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(subset):
                        subset = dp[j] + [nums[i]]
            dp[i] = subset
            if len(subset) > len(ans):
                ans = subset
        return ans