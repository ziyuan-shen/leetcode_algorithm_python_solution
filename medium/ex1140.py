class Solution:
    def optimize(self, idx, M, ps):
        if idx == len(ps) - 1:
            return 0
        if (idx, M) in self.mem:
            return self.mem[(idx, M)]
        else:
            ans = 0
            for x in range(1, min(2 * M, len(ps) - 1 - idx) + 1):
                ans = max(ans, ps[idx+x] - ps[idx] + (0 if (idx + x == len(ps) - 1) else (ps[-1] - ps[idx+x])) - self.optimize(idx+x, max(M, x), ps))
            self.mem[(idx, M)] = ans
            return ans
        
    def stoneGameII(self, piles: List[int]) -> int:
        self.mem = dict()
        ps = [0 for _ in range(len(piles) + 1)]
        for i in range(len(piles)):
            ps[i+1] = piles[i] + ps[i]
        return self.optimize(0, 1, ps)