from collections import defaultdict
import bisect
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.data[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        timestamps = list(self.data.keys())
        hits = list(self.data.values())
        leftidx = bisect.bisect(timestamps, timestamp - 300)
        rightidx = bisect.bisect(timestamps, timestamp)
        return sum(hits[leftidx:rightidx])

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)