from collections import deque
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = deque([])
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                ans.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return list(ans)