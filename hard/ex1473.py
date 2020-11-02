class Solution:
    def paint(self, idx, neighbornum, costtotal, houses, cost, m, n, target):
        if (idx, neighbornum, costtotal, houses[idx-1]) in self.mem:
            return self.mem[(idx, neighbornum, costtotal, houses[idx-1])]
        if idx == m:
            if neighbornum == target:
                self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = costtotal
            else:
                self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = float("inf")
        elif houses[idx] != 0:
            if idx == 0 or houses[idx] != houses[idx-1]:
                if neighbornum < target:
                    self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = self.paint(idx+1, neighbornum+1, costtotal, houses, cost, m, n, target)
                else:
                    self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = float("inf")
            elif neighbornum <= target:
                self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = self.paint(idx+1, neighbornum, costtotal, houses, cost, m, n, target)
            else:
                self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = float("inf")
        elif neighbornum == target:
            houses[idx] = houses[idx-1]
            self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = self.paint(idx+1, neighbornum, costtotal + cost[idx][houses[idx]-1], houses, cost, m, n, target)
            houses[idx] = 0
        elif neighbornum < target:
            ans = float("inf")
            for i in range(1, n+1):
                houses[idx] = i
                if idx == 0 or i != houses[idx-1]:
                    ans = min(ans, self.paint(idx+1, neighbornum + 1, costtotal + cost[idx][i-1], houses, cost, m, n, target))
                else:
                    ans = min(ans, self.paint(idx+1, neighbornum, costtotal + cost[idx][i-1], houses, cost, m, n, target))
                houses[idx] = 0
            self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = ans
        else:
            self.mem[(idx, neighbornum, costtotal, houses[idx-1])] = float("inf")
        return self.mem[(idx, neighbornum, costtotal, houses[idx-1])]
    
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.mem = dict()
        ans = self.paint(0, 0, 0, houses, cost, m, n, target)
        return ans if ans < float("inf") else -1