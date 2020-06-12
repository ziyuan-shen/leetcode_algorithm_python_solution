from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        nums = Counter(nums)
        ans = 0
        if k == 0:
            for num in nums:
                if nums[num] > 1:
                    ans += 1
        else:
            for num in nums:
                if (num + k) in nums:
                    ans += 1
        return ans