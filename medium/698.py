class Solution:
    def search(self, groupsum, nums, idx):
        if idx == len(nums):
            return True
        for group in groupsum:
            if groupsum[group] + nums[idx] <= self.target:
                groupsum[group] += nums[idx]
                if self.search(groupsum, nums, idx + 1):
                    return True
                groupsum[group] -= nums[idx]
            if not groupsum[group]:
                break
        return False
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        acc = sum(nums)
        if acc % k != 0:
            return False
        self.target = acc // k
        nums.sort(reverse=True)
        groupsum = {i: 0 for i in range(k)}
        return self.search(groupsum, nums, 0)