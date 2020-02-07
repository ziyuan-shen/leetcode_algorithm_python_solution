class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.filled = []

    def seat(self) -> int:
        if not self.filled:
            self.filled.append(0)
            return 0
        max_dis = 0
        if (self.filled[0] - 0) > max_dis:
            max_dis = self.filled[0] - 0
            idx = 0
            p = 0
        for i in range(1, len(self.filled)):
            if (self.filled[i] - self.filled[i-1]) // 2 > max_dis:
                max_dis = (self.filled[i] - self.filled[i-1]) // 2
                p = i
                idx = self.filled[i-1] + max_dis
        if (self.N - 1 - self.filled[-1]) > max_dis:
            max_dis = self.N - self.filled[-1]
            idx = self.N - 1
            p = len(self.filled)
        self.filled.insert(p, idx)
        return idx

    def leave(self, p: int) -> None:
        self.filled.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)