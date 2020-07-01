class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        ans = []
        if nums[0] != 1:
            ans.extend(list(range(1, nums[0])))
        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i] + 1:
                ans.extend(list(range(nums[i] + 1, nums[i+1])))
        if nums[-1] != len(nums):
            ans.extend(list(range(nums[-1] + 1, len(nums) + 1)))
        return ans