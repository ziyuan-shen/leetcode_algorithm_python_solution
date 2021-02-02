from collections import deque
import time
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = deque([])
        self.cap = capacity

    def enqueue(self, element: int) -> None:
        while len(self.q) == self.cap:
            time.sleep(0.1)
        self.q.append(element)

    def dequeue(self) -> int:
        while not self.q:
            time.sleep(0.1)
        return self.q.popleft()

    def size(self) -> int:
        return len(self.q)