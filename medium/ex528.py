import random
class Solution:
    def __init__(self, w: List[int]):
        self.cw = [0 for _ in range(len(w))]
        self.cw[0] = w[0]
        for i in range(1, len(w)):
            self.cw[i] = self.cw[i-1] + w[i]

    def pickIndex(self) -> int:
        return random.choices(range(len(self.cw)), cum_weights = self.cw)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()