class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product = [1] * length
        right_product = [1] * length
        product = [1] * length
        for i in range(1, length):
            left_product[i] = nums[i-1] * left_product[i-1]
        for i in range(length-2, -1, -1):
            right_product[i] = nums[i+1] * right_product[i+1]
        for i in range(length):
            product[i] = right_product[i] * left_product[i]
        return product