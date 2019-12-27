class Solution:
    def binarySearch(self, nums, target):
        if nums == []:
            return -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        length = len(nums)
        low = 0
        high = length - 1
        rotation_idx = 0
        if length > 1:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < nums[mid+1]:
                    if nums[mid] < nums[high]:
                        high = mid
                    else:
                        low = mid + 1
                else:
                    rotation_idx = mid + 1
                    break
        left = nums[:rotation_idx]
        right = nums[rotation_idx:]
        left_result = self.binarySearch(left, target)
        if left_result != -1:
            return left_result
        right_result = self.binarySearch(right, target)
        if right_result == -1:
            return -1
        else:
            return right_result + len(left)