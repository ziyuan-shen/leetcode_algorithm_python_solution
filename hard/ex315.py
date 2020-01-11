class Solution:
    def binarySearch(self, nums, start, target):
        low = start
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                if mid == len(nums) - 1 or nums[mid+1] >= target:
                    return mid + 1
                else:
                    low = mid + 1
            else:
                if mid == start or nums[mid-1] < target:
                    return mid
                else:
                    high = mid - 1
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            idx = self.binarySearch(nums, i+1, nums[i])
            ans[i] = idx - i - 1
            nums.insert(idx, nums[i])
            del nums[i]
        return ans
        