import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        A = []
        B = []
        idx = 0
        while idx < len(costs) and len(A) < n and len(B) < n:
            if costs[idx][0] <= costs[idx][1]:
                A.append(costs[idx])
            else:
                B.append(costs[idx])
            idx += 1
        A = [[cost[1]- cost[0], cost[0], cost[1]] for cost in A]
        B = [[cost[0] - cost[1], cost[0], cost[1]] for cost in B]
        heapq.heapify(A)
        heapq.heapify(B)
        if idx < len(costs):
            for cost in costs[idx:]:
                if len(A) == n:
                    if cost[0] + A[0][0] < cost[1]:
                        p = heapq.heappop(A)
                        heapq.heappush(A, [cost[1] - cost[0], cost[0], cost[1]])
                        heapq.heappush(B, [p[1] - p[2], p[1], p[2]])
                    else:
                        heapq.heappush(B, [cost[0]- cost[1], cost[0], cost[1]])
                else:
                    if cost[1] + B[0][0] < cost[0]:
                        p = heapq.heappop(B)
                        heapq.heappush(B, [cost[0] - cost[1], cost[0], cost[1]])
                        heapq.heappush(A, [p[2] - p[1], p[1], p[2]])
                    else:
                        heapq.heappush(A, [cost[1] - cost[0], cost[0], cost[1]])
        return sum([item[1] for item in A]) + sum([item[2] for item in B])
                        