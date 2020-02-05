from collections import Counter
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        ans = 0
        counts = Counter(A)
        nums = sorted(list(counts.keys()))
        minim = nums[0] - 1
        for num in nums:
            if num <= minim:
                ans += (minim - num + 1) * counts[num]
            ans += sum(list(range(1, counts[num])))
            minim = max(minim + 1, num) + counts[num] - 1
        return ans