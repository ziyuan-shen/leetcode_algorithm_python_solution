class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        change_flag = True
        while change_flag:
            change_flag = False
            for i in range(len(intervals)-1):
                for j in range(i+1, len(intervals)):
                    i1 = intervals[i]
                    i2 = intervals[j]
                    if not (i1[0]>i2[1] or i1[1]<i2[0]):
                        new = [min(i1[0], i2[0]), max(i1[1], i2[1])]
                        intervals.remove(i1)
                        intervals.remove(i2)
                        intervals.append(new)
                        change_flag = True
                        break
        return intervals