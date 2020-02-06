from bisect import bisect
from collections import defaultdict
class LogSystem:

    def __init__(self):
        self.iddic = defaultdict(set)
        self.time = []
        self.graToIdx = {"Year": 3, "Month": 6, "Day": 9, "Hour": 12, "Minute": 15, "Second": 18}

    def put(self, id: int, timestamp: str) -> None:
        idx = bisect(self.time, timestamp)
        self.time.insert(idx, timestamp)
        self.iddic[timestamp].add(id)

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        idx = self.graToIdx[gra]
        s = s[:idx + 1]
        e = e[:idx + 1]
        ans = []
        for timestamp in self.time:
            if timestamp[:idx + 1] >= s and timestamp[:idx + 1] <= e:
                ans.extend(list(self.iddic[timestamp]))
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)