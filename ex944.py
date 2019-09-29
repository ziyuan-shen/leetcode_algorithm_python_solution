class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        N = len(A[0])
        length = N
        for i in range(N):
            column = [A[j][i] for j in range(len(A))]
            if sorted(column)==column:
                length -= 1
        return length