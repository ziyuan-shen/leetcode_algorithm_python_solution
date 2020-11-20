from bisect import bisect
from collections import deque
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = deque([])
        q = deque([1])
        visited = {1}
        while len(ans) < n:
            num = q.popleft()
            ans.append(num)
            for prime in [2, 3, 5]:
                if num * prime not in visited:
                    visited.add(num * prime)
                    idx = bisect(q, num * prime)
                    q.insert(idx, num * prime)
        return ans[n-1]