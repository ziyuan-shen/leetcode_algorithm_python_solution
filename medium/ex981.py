import bisect
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([timestamp, value])
        else:
            self.data[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        else:
            idx = bisect.bisect(self.data[key], [timestamp, chr(126)]) - 1
            if idx != -1:
                return self.data[key][idx][1]
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)