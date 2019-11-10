class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutions = set()
        length = len(nums)
        for i in range(1, length-1):
            l = 0
            r = length-1
            while l<i and r>i:
                if nums[l]+nums[i]+nums[r]==0:
                    if (nums[l], nums[i], nums[r]) not in solutions:
                        solutions.add((nums[l], nums[i], nums[r]))
                    r -= 1
                    l += 1
                elif nums[l]+nums[i]+nums[r]>0:
                    r -= 1
                else:
                    l += 1
        return list(map(list, solutions))