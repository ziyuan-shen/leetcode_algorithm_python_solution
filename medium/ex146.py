class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.key_order = []
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.key_order.remove(key)
            self.key_order = [key] + self.key_order
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            self.key_order.remove(key)
            self.key_order = [key] + self.key_order
        else:
            if len(self.cache)<self.capacity:
                self.cache[key] = value
                self.key_order = [key]+self.key_order
            else:
                self.cache.pop(self.key_order[-1])
                self.cache[key] = value
                self.key_order = [key] + self.key_order[:-1]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)