class Solution:
    def countSmallerThan(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            elif mid == high or nums[mid+1] >= target:
                return mid + 1
            else:
                low = mid + 1
        return 0
            
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                ans += self.countSmallerThan(nums[j+1:], nums[i] + nums[j])
        return ans