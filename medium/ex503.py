from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [-1]
        q = deque(nums[1:])
        ans = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for idx in range(len(nums) - 1):
                if q[idx] > nums[i]:
                    ans[i] = q[idx]
                    break
            q.popleft()
            q.append(nums[i])
        return ans