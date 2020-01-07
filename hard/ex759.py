"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution: 
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append((interval.start, interval.end))
        intervals.sort()
        if len(intervals) <= 1:
            return []
        prev = intervals[0][1]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > prev:
                ans.append(Interval(prev, intervals[i][0]))
            prev = max(prev, intervals[i][1])
        return ans