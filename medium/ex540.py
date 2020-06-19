class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) // 2
        while low <= high:
            mid = (low + high) // 2
            if mid == low and mid == high:
                return nums[2 * mid]
            elif mid == low or mid == high:
                if nums[2 * low] == nums[2 * low + 1]:
                    return nums[2 * high]
                elif nums[2 * high - 1] == nums[2 * high]:
                    return nums[2 * low]
                else:
                    return nums[2 * low + 1]
            else:
                if nums[2 * mid] == nums[2 * mid - 1]:
                    high = mid - 1
                elif nums[2 * mid] == nums[2 * mid + 1]:
                    low = mid + 1
                else:
                    return nums[2 * mid]
                