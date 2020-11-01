class Solution:
    def paint(self, idx, neighbornum, costtotal, houses, cost, m, n, target):
        if idx == m:
            if neighbornum == target:
                self.ans = min(self.ans, costtotal)
        elif houses[idx] != 0:
            if idx == 0 or houses[idx] != houses[idx-1]:
                if neighbornum < target:
                    self.paint(idx+1, neighbornum+1, costtotal, houses, cost, m, n, target)
            elif neighbornum <= target:
                self.paint(idx+1, neighbornum, costtotal, houses, cost, m, n, target)
        elif neighbornum == target:
            houses[idx] = houses[idx-1]
            self.paint(idx+1, neighbornum, costtotal + cost[idx][houses[idx]-1], houses, cost, m, n, target)
            houses[idx] = 0
        elif neighbornum < target:
            for i in range(1, n+1):
                houses[idx] = i
                if idx == 0 or i != houses[idx-1]:
                    self.paint(idx+1, neighbornum + 1, costtotal + cost[idx][i-1], houses, cost, m, n, target)
                else:
                    self.paint(idx+1, neighbornum, costtotal + cost[idx][i-1], houses, cost, m, n, target)
                houses[idx] = 0
    
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.ans = float("inf")
        self.paint(0, 0, 0, houses, cost, m, n, target)
        return self.ans if self.ans != float("inf") else -1