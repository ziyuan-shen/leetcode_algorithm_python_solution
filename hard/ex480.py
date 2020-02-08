from collections import deque
class Solution:
    def median(self, nums, k):
        if k % 2 == 1:
            return nums[k//2]
        else:
            return (nums[k//2-1] + nums[k//2]) / 2
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = deque(nums[:k])
        ans = [self.median(sorted(window), k)]
        for i in range(k, len(nums)):
            window.popleft()
            window.append(nums[i])
            ans.append(self.median(sorted(window), k))
        return ans