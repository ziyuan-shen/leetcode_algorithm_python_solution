from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        twosum = []
        for i in range(len(A)):
            for j in range(len(B)):
                twosum.append(A[i] + B[j])
        hm = []
        for i in range(len(C)):
            for j in range(len(D)):
                hm.append(C[i] + D[j])
        hm = Counter(hm)
        ans = 0
        for num in twosum:
            if -num in hm:
                ans += hm[-num]
        return ans