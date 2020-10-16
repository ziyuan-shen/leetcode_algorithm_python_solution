class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            ps[i+1] = ps[i] + nums[i]
        for i in range(len(nums)):
            if ps[i+1] == (ps[-1] - ps[i]):
                return i
        return -1