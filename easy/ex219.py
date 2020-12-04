class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
                else:
                    seen[nums[i]] = i
            else:
                seen[nums[i]] = i
        return False