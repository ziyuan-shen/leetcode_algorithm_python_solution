from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counts = Counter(nums)
        nums = sorted(counts.keys())
        dp = [(nums[0] * counts[nums[0]], 0) for _ in range(len(counts))]
        for i in range(1, len(dp)):
            using, avoid = dp[i-1]
            if nums[i] > nums[i-1] + 1:
                dp[i] = (nums[i] * counts[nums[i]] + max(using, avoid), max(using, avoid))
            else:
                dp[i] = (nums[i] * counts[nums[i]] + avoid, max(using, avoid))
        return max(dp[-1])