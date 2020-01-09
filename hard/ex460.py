from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.data:
            value, freq = self.data.pop(key)
            self.data[key] = (value, freq + 1)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return None
        if key in self.data:
            old_value, freq = self.data.pop(key)
            self.data[key] = (value, freq + 1)
        else:
            if len(self.data) < self.cap:
                self.data[key] = (value, 1)
            else:
                orders = []
                for idx, k in enumerate(self.data):
                    orders.append((self.data[k][1], idx, k))
                orders.sort()
                remkey = orders[0][2]
                self.data.pop(remkey)
                self.data[key] = (value, 1)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)