from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mindeque = deque([0])
        maxdeque = deque([0])
        ans, left = 1, 0
        for i in range(1, len(nums)):
            while maxdeque and nums[i] >= nums[maxdeque[-1]]:
                maxdeque.pop()
            maxdeque.append(i)
            while mindeque and nums[i] <= nums[mindeque[-1]]:
                mindeque.pop()
            mindeque.append(i)
            if (nums[maxdeque[0]] - nums[mindeque[0]]) <= limit:
                ans = max(ans, i - left + 1)
            else:
                while (nums[maxdeque[0]] - nums[mindeque[0]]) > limit:
                    left += 1
                    if mindeque[0] < left:
                        mindeque.popleft()
                    if maxdeque[0] < left:
                        maxdeque.popleft()
        return ans