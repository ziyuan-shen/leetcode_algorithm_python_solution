class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        idx1, idx2 = 0, 1
        current = s[0]
        ans = 0
        while idx2 < len(s):
            if s[idx2] == current:
                if cost[idx2] > cost[idx1]:
                    ans += cost[idx1]
                    idx1 = idx2
                else:
                    ans += cost[idx2]
            else:
                current = s[idx2]
                idx1 = idx2
            idx2 += 1
        return ans