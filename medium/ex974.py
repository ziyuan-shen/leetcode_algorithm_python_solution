from collections import Counter
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ps = [0 for _ in range(len(A) + 1)]
        ans = 0
        for i in range(1, len(A) + 1):
            ps[i] = (ps[i-1] + A[i-1]) % K
        return sum([v * (v - 1) // 2 for v in Counter(ps).values()])