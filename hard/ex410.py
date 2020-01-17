class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(len(nums))]
        cum = [sum(nums[:i+1]) for i in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = cum[i]
        for j in range(1, m):
            for i in range(j, len(nums)):
                dp[i][j] = min([max(dp[k][j-1], cum[i]-cum[k]) for k in range(j-1, i)])
        return dp[-1][-1]