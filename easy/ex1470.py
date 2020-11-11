class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i % 2 == 0:
                ans[i] = nums[i // 2]
            else:
                ans[i] = nums[len(nums) // 2 + i // 2]
        return ans