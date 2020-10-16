class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = nums[0]
        least = total
        for num in nums[1:]:
            total += num
            least = min(least, total)
        return max(1, 1 - least)