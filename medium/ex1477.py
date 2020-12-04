class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        subarrays = []
        p1, p2 = 0, 0
        total = arr[p1]
        while p2 < len(arr) - 1 or (total == target and p2 < len(arr)):
            while p2 + 1 < len(arr) and total + arr[p2 + 1] <= target:
                p2 += 1
                total += arr[p2]
            if total < target and p2 + 1 < len(arr):
                p2 += 1
                total += arr[p2]
            if total > target:
                while p1 < p2 and total > target:
                    total -= arr[p1]
                    p1 += 1
            if total == target:
                subarrays.append([p1, p2])
                if p1 < p2:
                    total -= arr[p1]
                    p1 += 1
                else:
                    p2 += 1
                    p1 = p2
                    if p2 < len(arr):
                        total = arr[p2]                
            elif total > target:
                p2 += 1
                p1 = p2
                if p2 < len(arr):
                    total = arr[p2]
        if len(subarrays) < 2:
            return -1
        minarr = [-1 for _ in range(len(arr))]
        minlen = float("inf")
        for s in subarrays:
            l = s[1] - s[0] + 1
            if l < minlen:
                minlen = l
                minarr[s[1]:] = [l] * (len(arr) - s[1])
        ans = float("inf")
        for s in subarrays:
            if s[0] - 1 >= 0 and minarr[s[0] - 1] != -1:
                ans = min(ans, s[1] - s[0] + 1 + minarr[s[0] - 1])
        return ans if ans != float("inf") else -1