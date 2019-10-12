class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[-i-1] == 0:
                for j in range(-i-1, -1):
                    nums[j] = nums[j+1]
                nums[-1] = 0