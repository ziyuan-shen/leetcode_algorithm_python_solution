class Solution:
    def roll(self, rem, num, cons, rollMax):
        if (rem, num, cons) in self.mem:
            return self.mem[(rem, num, cons)]
        if rem == 0:
            return 1
        ans = 0
        for i in range(1, 7):
            if i == num:
                if cons < rollMax[i-1]:
                    ans += self.roll(rem-1, num, cons+1, rollMax)
            else:
                ans += self.roll(rem-1, i, 1, rollMax)
        self.mem[(rem, num, cons)] = ans % (10 ** 9 + 7)
        return ans % (10 ** 9 + 7)
    
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.mem = dict()
        ans = 0
        for i in range(1, 7):
            ans += self.roll(n-1, i, 1, rollMax)
        return ans % (10 ** 9 + 7)