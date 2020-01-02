class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
    
    def binarySearch(self, l, target):
        low = 0
        high = len(l) - 1
        while low <= high:
            mid = (low + high) // 2
            if l[mid] <= target:
                if mid == len(l) - 1 or l[mid+1] > target:
                    return mid
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([timestamp, value])
        else:
            self.data[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        else:
            idx = self.binarySearch([x[0] for x in self.data[key]], timestamp)
            if idx != -1:
                return self.data[key][idx][1]
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)