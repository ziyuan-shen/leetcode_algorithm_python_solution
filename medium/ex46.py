class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = {(nums[i],): nums[:i] + nums[i+1:] for i in range(len(nums))}
        for _ in range(len(nums)-1):
            for permute in list(ans):
                remaining = ans[permute]
                for i in range(len(remaining)):
                    ans[permute+(remaining[i],)] = remaining[:i] + remaining[i+1:]
                ans.pop(permute)
        return [list(permute) for permute in ans]