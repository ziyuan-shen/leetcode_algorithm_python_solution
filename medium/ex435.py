class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        ans = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end:
                ans += 1
                end = min(interval[1], end)
            else:
                end = interval[1]
        return ans