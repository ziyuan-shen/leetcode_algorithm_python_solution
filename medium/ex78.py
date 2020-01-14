class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            new = []
            for t in ans:
                new.append(t + [num])
            ans.extend(new)
        return ans