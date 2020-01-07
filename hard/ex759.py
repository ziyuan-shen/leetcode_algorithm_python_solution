"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def getFreeTime(self, intervals):
        freetime = []
        if intervals[0].start > self.starttime:
            freetime.append(Interval(self.starttime, intervals[0].start))
        for i in range(len(intervals)-1):
            if intervals[i].end < intervals[i+1].start:
                freetime.append(Interval(intervals[i].end, intervals[i+1].start))
        if intervals[-1].end < self.endtime:
            freetime.append(Interval(intervals[-1].end, self.endtime))
        return freetime
        
    def getCommonTime(self, intervals1, intervals2):
        commontime = []
        for interval2 in intervals2:
            if intervals1 and interval2.end <= intervals1[0].start:
                continue
            else:
                while intervals1 and interval2.end > intervals1[0].start:
                    if intervals1[0].end <= interval2.start:
                        intervals1.pop(0)
                        continue
                    commontime.append(Interval(max(interval2.start, intervals1[0].start), min(interval2.end, intervals1[0].end)))
                    if interval2.end < intervals1[0].end:
                        intervals1[0].start = interval2.end
                    else:
                        intervals1.pop(0)
        return commontime
        
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        start = float("inf")
        end = float("-inf")
        for employee in schedule:
            if employee[0].start < start:
                start = employee[0].start
            if employee[-1].end > end:
                end = employee[-1].end
        self.starttime = start
        self.endtime = end
        freetimes = []
        for employee in schedule:
            freetime = self.getFreeTime(employee)
            if freetime:
                freetimes.append(freetime)
        if not freetimes:
            return []
        commontime = freetimes[0]
        for i in range(1, len(freetimes)):
            commontime = self.getCommonTime(commontime, freetimes[i])
        return commontime
        