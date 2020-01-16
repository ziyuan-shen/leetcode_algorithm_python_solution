from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        cumdict = defaultdict(list)
        cumdict[0] = [-1]
        for idx in range(len(nums)):
            if nums[idx] == 0:
                count -= 1
            else:
                count += 1
            cumdict[count].append(idx)
        ans = 0
        for l in cumdict.values():
            if len(l) >= 2:
                ans = max(ans, l[-1] - l[0])
        return ans