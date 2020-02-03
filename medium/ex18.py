class Solution:
    def threeSum(self, nums, target):
        ans = set()
        for i in range(1, len(nums) - 1):
            left = 0
            right = len(nums) - 1
            while left < i and right > i:
                if nums[left] + nums[i] + nums[right] == target:
                    ans.add((nums[left], nums[i], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[i] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return ans
                    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            if target >= 4 * nums[i]:
                threesums = self.threeSum(nums[i+1:], target - nums[i])
                for threesum in threesums:
                    ans.add((nums[i],) + threesum)
        return [list(foursum) for foursum in ans]