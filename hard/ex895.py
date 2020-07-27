class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = {}
        self.last_idx = {}
        self.max_count = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x not in self.count:
            self.count[x] = 1
        else:
            self.count[x] += 1
        self.max_count = max(self.max_count, self.count[x])
        self.last_idx[x] = len(self.stack) - 1

    def pop(self) -> int:
        pop_idx = 0
        for x, count in self.count.items():
            if count == self.max_count:
                if self.last_idx[x] >= pop_idx:
                    pop_idx = self.last_idx[x]
                    pop_x = x
        if self.max_count == 1:
            self.count.pop(pop_x)
            self.last_idx.pop(pop_x)
        else:
            self.count[pop_x] -= 1
            for i in range(pop_idx - 1, -1, -1):
                if self.stack[i] == pop_x:
                    self.last_idx[pop_x] = i
                    break
        if self.count:
            self.max_count = max(self.count.values())
        else:
            self.max_count = 0
        for x, idx in self.last_idx.items():
            if idx > pop_idx:
                self.last_idx[x] -= 1
        del self.stack[pop_idx]
        return pop_x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()