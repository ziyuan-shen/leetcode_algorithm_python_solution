from collections import deque
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = {}
        self.LRU = deque([])

    def get(self, key: int) -> int:
        if key in self.data:
            self.LRU.remove(key)
            self.LRU.append(key)
            value, freq = self.data[key]
            self.data[key] = (value, freq + 1)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return None
        if key in self.data:
            freq = self.data[key][1]
            self.data[key] = (value, freq + 1)
            self.LRU.remove(key)
            self.LRU.append(key)
        else:
            if len(self.data) < self.cap:
                self.data[key] = (value, 1)
                self.LRU.append(key)
            else:
                freqs = [(self.data[k][1], k) for k in self.data]
                freqs.sort()
                minfreq = freqs[0][0]
                remkey = freqs[0][1]
                if len(freqs) > 1 and freqs[1][0] == minfreq:
                    idx = 1
                    while idx < len(freqs) and freqs[idx][0] == minfreq:
                        if self.LRU.index(freqs[idx][1]) < self.LRU.index(remkey):
                            remkey = freqs[idx][1]
                        idx += 1
                self.data.pop(remkey)
                self.LRU.remove(remkey)
                self.data[key] = (value, 1)
                self.LRU.append(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)