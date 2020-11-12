class Solution:
    def roll(self, total, diceleft, f, target):
        if (total, diceleft) in self.mem:
            return self.mem[(total, diceleft)]
        if diceleft * f < target - total:
            self.mem[(total, diceleft)] = 0
            return 0
        if diceleft == 1:
            if target - total >= 1 and target - total <= f:
                self.mem[(total, diceleft)] = 1
            else:
                self.mem[(total, diceleft)] = 0
            return self.mem[(total, diceleft)]
        ans = 0
        for num in range(1, f+1):
            if num + total < target:
                ans += self.roll(total + num, diceleft - 1, f, target)
        self.mem[(total, diceleft)] = ans % (10 ** 9 + 7)
        return ans % (10 ** 9 + 7)
        
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d:
            return 0
        self.mem = dict()
        return self.roll(0, d, f, target)