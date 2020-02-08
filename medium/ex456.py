class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        s1 = 0
        risings = []
        while s1 + 1 < len(nums):
            while s1 + 1 < len(nums) and nums[s1+1] <= nums[s1]:
                s1 += 1
            if s1 + 1 < len(nums):
                s2 = s1 + 1
                while s2 + 1 < len(nums) and nums[s2+1] >= nums[s2]:
                    s2 += 1
                risings.append((s1, s2))
                s1 = s2 + 1
        for s1, s2 in risings:
            for k in range(s2 + 1, len(nums)):
                if nums[s1] < nums[k] and nums[k] < nums[s2]:
                    return True
        return False