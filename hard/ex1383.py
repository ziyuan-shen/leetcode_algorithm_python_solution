import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        combo = [[efficiency[i], speed[i]] for i in range(n)]
        combo.sort()
        people_num = 0
        speed_total = 0
        current_performance = 0
        q = []
        heapq.heapify(q)
        ans = float("-inf")
        for c in combo[::-1]:
            if people_num < k:
                current_performance = (c[1] + speed_total) * c[0]
                ans = max(ans, current_performance)
                speed_total += c[1]
                people_num += 1
                heapq.heappush(q, c[1])
            else:
                if c[1] > q[0]:
                    current_performance = (c[1] - q[0] + speed_total) * c[0]
                    ans = max(ans, current_performance)
                    speed_total += c[1] - q[0]
                    heapq.heappop(q)
                    heapq.heappush(q, c[1])
        return ans % (10 ** 9 + 7)