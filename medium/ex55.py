class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nearest_true = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nearest_true - i <= nums[i]:
                nearest_true = i
        return nearest_true == 0