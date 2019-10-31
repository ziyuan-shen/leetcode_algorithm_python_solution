class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        rob_list = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            rob_list.append(max(rob_list[i-2]+nums[i], rob_list[i-1]))
        return rob_list[-1]