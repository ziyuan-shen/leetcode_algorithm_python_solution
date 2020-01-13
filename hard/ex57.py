class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        flag = True
        while idx < len(intervals):
            if newInterval[1] < intervals[idx][0]:
                intervals.insert(idx, newInterval)
                flag = False
                break
            if newInterval[0] > intervals[idx][1]:
                idx += 1
            else:
                left = min(intervals[idx][0], newInterval[0])
                while idx < len(intervals) and newInterval[1] >= intervals[idx][0]:
                    right = max(intervals[idx][1], newInterval[1])
                    del intervals[idx]
                intervals.insert(idx, [left, right])
                flag = False
                break
        if flag:
            intervals.append(newInterval)
        return intervals