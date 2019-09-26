class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = '{0:032b}'.format(x)
        y_bin = '{0:032b}'.format(y)
        self.ans = 0
        for i in range(32):
            if y_bin[i] != x_bin[i]:
                self.ans += 1
        return self.ans
