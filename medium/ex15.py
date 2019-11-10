class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        two_list = []
        solutions = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if not ([nums[i], nums[j]] in two_list or [nums[j], nums[i]] in two_list):
                    two_list.append([nums[i], nums[j]])
                    third = 0 - nums[i] - nums[j]
                    if third in nums[j+1:]:
                        solutions.append([nums[i], nums[j], third])
        return solutions