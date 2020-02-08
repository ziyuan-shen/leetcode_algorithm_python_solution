class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        cumsum = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(cumsum)):
            cumsum[i] = cumsum[i-1] + nums[i-1]
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if k == 0:
                    if cumsum[j+1] - cumsum[i] == 0:
                        return True
                elif (cumsum[j+1] - cumsum[i]) % k == 0:
                    return True
        return False