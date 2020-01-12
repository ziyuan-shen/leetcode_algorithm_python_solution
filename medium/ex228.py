class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        idx = 0
        while idx < len(nums):
            if idx == len(nums) - 1:
                ans.append(str(nums[idx]))
                idx += 1
            else:
                left = nums[idx]
                right = left
                idx += 1
                while idx < len(nums) and nums[idx] == nums[idx-1] + 1:
                    right = nums[idx]
                    idx += 1
                if right == left:
                    ans.append(str(right))
                else:
                    ans.append(str(left) + "->" + str(right))
        return ans