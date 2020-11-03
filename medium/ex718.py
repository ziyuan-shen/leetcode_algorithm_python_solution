class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            count = 0
            for idx in range(i, len(A)):
                if A[idx] == B[idx - i]:
                    count += 1
                    ans = max(count, ans)
                else:
                    count = 0
        for i in range(len(A)):
            count = 0
            for idx in range(i, len(A)):
                if B[idx] == A[idx - i]:
                    count += 1
                    ans = max(count, ans)
                else:
                    count = 0
        return ans