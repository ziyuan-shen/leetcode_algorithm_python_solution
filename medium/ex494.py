class Solution:
    def addNum(self, current, idx, nums, target):
        if idx == len(nums):
            if current == target:
                self.memo[(current, idx)] = 1
                return 1
            else:
                self.memo[(current, idx)] = 0
                return 0
        else:
            if (current, idx) in self.memo:
                return self.memo[(current, idx)]
            else:
                add = self.addNum(current + nums[idx], idx + 1, nums, target)
                sub = self.addNum(current - nums[idx], idx + 1, nums, target)
                self.memo[(current, idx)] = add + sub
                return add + sub
        
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = {}
        return self.addNum(0, 0, nums, S)
        