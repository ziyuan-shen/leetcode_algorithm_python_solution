class Solution:
    def getDivisors(self, N):
        ans = [1]
        for i in range(2, int(N ** 0.5)):
            if N % i == 0:
                ans.append(i)
                ans.append(N / i)
        return ans
    
    def play(self, N):
        if N == 1:
            return False
        if N in self.mem:
            return self.mem[N]
        divisors = self.getDivisors(N)
        for div in divisors:
            if not self.play(N - div):
                self.mem[N] = True
                return True
        self.mem[N] = False
        return False
    
    def divisorGame(self, N: int) -> bool:
        self.mem = dict()
        return self.play(N)