class Solution:
    def partialSort(self, l, k):
        for i in range(k+1, len(l)):
            for j in range(len(l)-1, i-1, -1):
                if l[j] < l[j-1]:
                    temp = l[j]
                    l[j] = l[j-1]
                    l[j-1] = temp
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return None
        if nums[-1] > nums[-2]:
            temp = nums[-1]
            nums[-1] = nums[-2]
            nums[-2] = temp
            return None
        peak = -1
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] >= nums[i-1] and nums[i] >= nums[i+1]:
                peak = i
                for i in range(len(nums) - 1, peak - 1, -1):
                    if nums[i] > nums[peak-1]:
                        temp = nums[i]
                        nums[i] = nums[peak-1]
                        nums[peak-1] = temp
                        self.partialSort(nums, peak)
                        return None              
        self.partialSort(nums, 0)     