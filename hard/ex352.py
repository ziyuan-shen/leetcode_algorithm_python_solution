from bisect import bisect
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def addNum(self, val: int) -> None:
        idx = bisect(self.data, val)
        self.data.insert(idx, val)

    def getIntervals(self) -> List[List[int]]:
        if not self.data:
            return []
        intervals = [[self.data[0], self.data[0]]]
        for i in range(1, len(self.data)):
            if self.data[i] == self.data[i-1]:
                continue
            elif self.data[i] == self.data[i-1] + 1:
                intervals[-1][1] = self.data[i]
            else:
                intervals.append([self.data[i], self.data[i]])
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()