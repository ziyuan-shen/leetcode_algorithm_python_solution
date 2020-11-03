class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        p1 = 0
        p2 = len(A) - 1
        lead0, trail0 = 0, 0
        while p1 < len(A) and A[p1] == 0:
            lead0 += 1
            p1 += 1
        while p2 >= 0 and A[p2] == 0:
            trail0 += 1
            p2 -= 1
        if p1 > p2:
            return K
        groups = {1: [], 0: []}
        current = 0
        count = 0
        for i in range(p1, p2 + 1):
            if A[i] != current:
                groups[current].append(count)
                current = A[i]
                count = 1
            else:
                count += 1
        groups[1].append(count)
        groups[0].pop(0)
        if not groups[0]:
            return groups[1][0] + min(K, lead0 + trail0)
        zeros = [lead0] + groups[0] + [trail0]
        ones = groups[1]
        p1, p2 = 1, 1
        total0 = zeros[1]
        ans = 0
        while p2 < len(zeros) - 1:
            if total0 > K:
                ans = max(ans, ones[p1-1] + K)
                p1 += 1
                p2 += 1
                if p2 < len(zeros) - 1:
                    total0 = zeros[p2]
            else:
                while p2 + 1 < len(zeros) -1 and total0 + zeros[p2 + 1] <= K:
                    p2 += 1
                    total0 += zeros[p2]
                ans = max(ans, sum(ones[p1-1:p2+1]) + total0 + min(K-total0, zeros[p1-1] + zeros[p2+1]))
                total0 -= zeros[p1]
                p1 += 1
                if p2 < p1:
                    p2 += 1
                    total0 = zeros[p2]
        ans = max(ans, ones[-1] + min(K, zeros[-1] + zeros[-2]))
        return ans