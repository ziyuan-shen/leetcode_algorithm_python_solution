import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        idx = bisect.bisect(self.data, num)
        self.data.insert(idx, num)

    def findMedian(self) -> float:
        length = len(self.data)
        if length % 2 == 1:
            return self.data[int((length-1)/2)]
        else:
            return (self.data[int(length/2)] + self.data[int(length/2) - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()