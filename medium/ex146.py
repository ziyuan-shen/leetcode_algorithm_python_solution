from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.data:
            self.data.move_to_end(key)
            return self.data[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.pop(key)
            self.data[key] = value
        else:
            if len(self.data) == self.capacity:
                self.data.popitem(last=False)
                self.data[key] = value
            else:
                self.data[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)