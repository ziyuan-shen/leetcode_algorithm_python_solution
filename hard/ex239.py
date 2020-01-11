from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums
        q = deque([])
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]
        for i in range(k, len(nums)):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans