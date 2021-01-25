class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        rem = 1
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                if rem == 0:
                    return False
                else:
                    if idx == 0 or nums[idx - 1] <= nums[idx + 1]:
                        rem -= 1
                    elif idx + 1 == len(nums) - 1 or nums[idx] <= nums[idx + 2]:
                        rem -= 1
                    else:
                        return False
        return True