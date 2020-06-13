from collections import defaultdict
class Solution:
    def firstLargerThan(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if mid < len(nums) - 1:
                    return nums[mid+1]
                else:
                    return -1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid == 0 or nums[mid-1] <= target:
                    return nums[mid]
                else:
                    high = mid - 1
        return -1
        
    def minWindow(self, S: str, T: str) -> str:
        if not T or not S:
            return ""
        dic = defaultdict(list)
        for idx, letter in enumerate(S):
            dic[letter].append(idx)
        if T[0] not in dic:
            return ""
        ans = []
        length = float("inf")
        for start in dic[T[0]]:
            end = start
            for letter in T[1:]:
                end = self.firstLargerThan(dic[letter], end)
                if end == -1:
                    break
            if end != -1 and (end - start + 1) <= length:
                ans.append((start, end))
                length = end - start + 1
        if not ans:
            return ""
        ans = list(filter(lambda x: (x[1] - x[0] + 1) == length, ans))
        ans = [S[t[0]:t[1]+1] for t in ans]
        ans.sort()
        return ans[0]
                