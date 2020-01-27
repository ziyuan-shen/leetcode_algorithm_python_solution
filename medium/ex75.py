class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        one_count = 0
        two_count = 0
        i = 0
        while i < len(nums) - two_count:
            if nums[i] == 0:
                nums[i] = nums[zero_count]
                nums[zero_count] = 0
                zero_count += 1
                i += 1
            elif nums[i] == 1:
                one_count += 1
                i += 1
            else:
                two_count += 1
                nums[i] = nums[-two_count]
                nums[-two_count] = 2
        return nums