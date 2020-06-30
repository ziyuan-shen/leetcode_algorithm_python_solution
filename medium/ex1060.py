class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        miss_count = 0
        for i in range(len(nums) - 1):
            miss_count += nums[i+1] - nums[i] - 1
            if miss_count < k:
                continue
            else:
                return list(range(nums[i+1]-1, nums[i], -1))[miss_count-k]
        return nums[-1] + k - miss_count