from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if len(set(A)) < K:
            return 0
        d = Counter(A[:K])
        ans = 0
        p1 = 0
        p2 = K
        while p2 < len(A) and len(d) < K:
            if A[p2] in d:
                d[A[p2]] += 1
            else:
                d[A[p2]] = 1
            p2 += 1
        if len(d) == K:
            while True:
                while True:
                    p = p1
                    d2 = d.copy()
                    while len(d2) == K:
                        ans += 1
                        if d2[A[p]] == 1:
                            d2.pop(A[p])
                        else:
                            d2[A[p]] -= 1
                        p += 1
                    if p2 < len(A) and A[p2] in d:
                        d[A[p2]] += 1
                        p2 += 1
                    else:
                        break
                if p2 < len(A):
                    d[A[p2]] = 1
                    p2 += 1
                    while len(d) > K:
                        if d[A[p1]] == 1:
                            d.pop(A[p1])
                        else:
                            d[A[p1]] -= 1
                        p1 += 1
                else:
                    break
        return ans