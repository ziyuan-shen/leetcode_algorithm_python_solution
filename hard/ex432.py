class Node(object):
    def __init__(self, value):
        self.value = value
        self.keys = set()
        self.prev = None
        self.next = None
    
    def insert(self, node):
        nextnode = self.next
        self.next = node
        node.prev = self
        node.next = nextnode
        if nextnode:
            nextnode.prev = node
    
    def remove(self):
        prevnode = self.prev
        if prevnode:
            prevnode.next = self.next
        if self.next:
            self.next.prev = prevnode

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        self.head.insert(self.tail)
        self.dic = {}   #{key: node}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.dic:
            node = self.dic[key]
            if node.next.value == node.value + 1:
                node.next.keys.add(key)
                self.dic[key] = node.next
                node.keys.remove(key)
                if len(node.keys) == 0:
                    node.remove()
            elif len(node.keys) == 1:
                node.value += 1
            else:
                node.keys.remove(key)
                newnode = Node(node.value + 1)
                newnode.keys = {key}
                node.insert(newnode)
                self.dic[key] = newnode
        else:
            if self.head.next.value == 1:
                self.head.next.keys.add(key)
                self.dic[key] = self.head.next
            else:
                newnode = Node(1)
                newnode.keys = {key}
                self.head.insert(newnode)
                self.dic[key] = newnode

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.dic:
            node = self.dic[key]
            node.keys.remove(key)
            self.dic.pop(key)
            if node.value != 1:
                prevnode = node.prev
                if prevnode.value == (node.value - 1):
                    prevnode.keys.add(key)
                    self.dic[key] = prevnode
                else:
                    newnode = Node(node.value - 1)
                    newnode.keys.add(key)
                    prevnode.insert(newnode)
                    self.dic[key] = newnode
            if len(node.keys) == 0:
                node.remove()
                

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        node = self.tail.prev
        for key in node.keys:
            return key
        return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        node = self.head.next
        for key in node.keys:
            return key
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()