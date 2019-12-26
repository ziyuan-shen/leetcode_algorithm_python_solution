class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cum_sum = {0: 1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            ans += cum_sum.get(total - k, 0)
            if total in cum_sum:
                cum_sum[total] += 1
            else:
                cum_sum[total] = 1
        return ans