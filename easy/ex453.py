class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            ans += nums[i] - nums[0]
        return ans