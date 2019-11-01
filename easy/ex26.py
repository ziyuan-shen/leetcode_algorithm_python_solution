class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        nums.sort()
        idx = 0
        while (idx+1)<len(nums):
            while (idx+1)<len(nums) and nums[idx+1]==nums[idx]:
                nums.remove(nums[idx+1])
            idx += 1
        return len(nums)