class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        resabs = float("inf")
        res = 0
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == target:
                    return target
                elif sum3 < target:
                    if target - sum3 < resabs:
                        resabs = target - sum3
                        res = target - sum3
                    l += 1
                else:
                    if sum3 - target < resabs:
                        resabs = sum3 - target
                        res = target - sum3
                    r -= 1
        return target - res