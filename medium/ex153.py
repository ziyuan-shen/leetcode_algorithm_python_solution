class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid == low or mid == high:
                return min(nums[low], nums[high])
            elif nums[low] > nums[mid]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid
            else:
                return nums[low]