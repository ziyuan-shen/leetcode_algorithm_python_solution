class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                total = target - (nums[i] + nums[j])
                p1, p2 = j + 1, len(nums) - 1
                while p1 < p2:
                    if nums[p1] + nums[p2] == total:
                        ans.add((nums[i], nums[j], nums[p1], nums[p2]))
                        p1 += 1
                        p2 -= 1
                    elif nums[p1] + nums[p2] < total:
                        p1 += 1
                    else:
                        p2 -= 1
        return [list(t) for t in ans]