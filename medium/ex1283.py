from math import ceil

class Solution:
    def getSum(self, nums, divisor):
        ans = 0
        for num in nums:
            ans += ceil(num / divisor)
        return ans
        
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        low = ceil(nums[0] / (threshold // len(nums)))
        high = nums[-1]
        mid = (low + high) // 2
        while low <= high:
            if self.getSum(nums, mid) > threshold:
                low = mid + 1
                mid = (low + high) // 2
            else:
                if mid == 1 or self.getSum(nums, mid - 1) > threshold:
                    return mid
                else:
                    high = mid - 1
                    mid = (low + high) // 2