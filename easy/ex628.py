class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        idx = 0
        while idx < len(nums) and nums[idx] < 0:
            idx += 1
        if len(nums) - idx >= 3:
            return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        elif len(nums) - idx >= 1:
            return nums[0] * nums[1] * nums[-1]
        else:
            return nums[idx-1] * nums[idx-2] * nums[idx-3]