from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        ps = [0 for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            ps[i] = ps[i-1] + A[i-1]
        q = deque([0])
        ans = float("inf")
        for idx in range(1, len(A) + 1):
            while q and ps[idx] <= ps[q[-1]]:
                q.pop()
            while q and ps[idx] - ps[q[0]] >= K:
                ans = min(ans, idx - q[0])
                q.popleft()
            q.append(idx)
        return ans if ans != float("inf") else -1