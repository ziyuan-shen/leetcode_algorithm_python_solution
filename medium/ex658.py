from bisect import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect(arr, x)
        p1 = idx - 1
        p2 = idx
        for _ in range(k):
            if p1 >= 0 and p2 < len(arr):
                if x - arr[p1] <= arr[p2] - x:
                    p1 -= 1
                else:
                    p2 += 1
        if p1 < 0:
            return arr[:k]
        elif p2 > len(arr) - 1:
            return arr[-k:]
        else:
            return arr[p1+1:p2]