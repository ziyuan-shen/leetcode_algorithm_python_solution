class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indices = list(filter(lambda x: nums[x] % 2 == 1, range(len(nums))))
        if len(odd_indices) < k:
            return 0
        p1 = 0
        p2 = odd_indices[k-1]
        ans = 0
        for i in range(len(odd_indices[:-k]) + 1):
            if i+k < len(odd_indices):
                ans += (odd_indices[i] - p1 + 1) * (odd_indices[i+k] - p2)
                p1 = odd_indices[i] + 1
                p2 = odd_indices[i+k]
            else:
                ans += (odd_indices[i] - p1 + 1) * (len(nums) - p2)
        return ans