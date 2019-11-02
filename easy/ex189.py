class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return []
        if k % len(nums) != 0:
            k = k % len(nums)
            temp = nums[-k:]
            for j in range(len(nums)-1, k-1, -1):
                nums[j] = nums[j-k]
            nums[:k] = temp