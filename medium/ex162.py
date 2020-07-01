class Solution:
    def findPeak(self, nums):
        low = 1
        high = len(nums) - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[low] + mid - low:
                high = mid - 1
            elif nums[high] < nums[mid] + high - mid:
                low = mid + 1
            else:
                left = self.findPeak(nums[:mid+1])
                if left != -1:
                    return left
                right = self.findPeak(nums[mid:])
                if right != -1:
                    return mid + right
                return -1
        return -1
    
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, float("-inf"))
        nums.append(float("-inf"))
        return self.findPeak(nums) - 1