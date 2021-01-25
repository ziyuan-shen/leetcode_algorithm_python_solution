from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        d = defaultdict(list)
        for idx in range(len(ring)):
            d[ring[idx]].append(idx)
        dp = [[0 for _ in range(len(ring))] for _ in range(len(key))]
        for i in range(len(ring)):
            if key[-1] == ring[i]:
                dp[-1][i] = 1
            else:
                dist = float("inf")
                for idx in d[key[-1]]:
                    dist = min(dist, abs(idx - i), len(ring) - abs(idx - i))
                dp[-1][i] = dist + 1
        for i in range(len(key)-2, -1, -1):
            for j in range(len(ring)):
                if key[i] == ring[j]:
                    dp[i][j] = 1 + dp[i+1][j]
                else:
                    dist = float("inf")
                    for idx in d[key[i]]:
                        dist = min(dist, min(abs(idx - j), len(ring) - abs(idx - j)) + 1 + dp[i+1][idx])
                    dp[i][j] = dist
        print(dp)
        return dp[0][0]