class Solution:
    def dfs(self, nums, current_sum, idx, candidates, ans, target):
        for i in range(idx, len(candidates)):
            if current_sum + candidates[i] == target:
                ans.add(nums + (candidates[i],))
            elif current_sum + candidates[i] < target:
                self.dfs(nums+(candidates[i],), current_sum + candidates[i], i+1, candidates, ans, target)
            else:
                break
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        self.dfs((), 0, 0, candidates, ans, target)
        return [list(t) for t in ans]
                