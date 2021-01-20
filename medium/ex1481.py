from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        counts = list(counts.values())
        counts.sort()
        while k > 0 and counts:
            if counts[0] > k:
                k = 0
            else:
                k -= counts[0]
                counts.pop(0)
        return len(counts)