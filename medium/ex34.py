class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                left = self.searchRange(nums[:mid], target)
                right = self.searchRange(nums[mid+1:], target)
                start = mid
                end = mid
                if left[0] != -1:
                    start = left[0]
                if right[1] != -1:
                    end = mid +right[1] + 1
                return [start, end]
        return [-1, -1]