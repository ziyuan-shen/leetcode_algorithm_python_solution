class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = sorted(nums)
        left = 0
        while left < len(nums) and nums[left] == nums_copy[left]:
            left += 1
        right = len(nums) - 1
        while right >= 0 and nums[right] == nums_copy[right]:
            right -= 1
        return max(0, right - left + 1)