class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        left_product = nums[0]
        for i in range(1, len(nums)):
            ans[i] = left_product
            left_product *= nums[i]
        right_product = nums[-1]
        ans[0] = 1
        for i in range(len(nums) - 2, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        return ans