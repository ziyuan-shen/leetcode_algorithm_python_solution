class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums) // 2
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            if dic[num] > length:
                return num