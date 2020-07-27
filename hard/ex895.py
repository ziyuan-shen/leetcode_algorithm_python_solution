from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.stack = defaultdict(list)
        self.max_count = 0

    def push(self, x: int) -> None:
        self.count[x] += 1
        self.stack[self.count[x]].append(x)
        self.max_count = max(self.max_count, self.count[x])

    def pop(self) -> int:
        pop_x = self.stack[self.max_count].pop()
        self.count[pop_x] -= 1
        if not self.stack[self.max_count]:
            self.max_count -= 1
        return pop_x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()