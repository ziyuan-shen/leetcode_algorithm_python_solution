class Solution:
    def twoSumSmaller(self, nums, target):
        ans = 0
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] >= target:
                end -= 1
            else:
                ans += end - start
                start += 1
        return ans
        
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            ans += self.twoSumSmaller(nums[i+1:], target - nums[i])
        return ans