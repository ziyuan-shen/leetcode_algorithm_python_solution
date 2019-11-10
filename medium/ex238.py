class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    product[j] = product[j] * nums[i]
        return product