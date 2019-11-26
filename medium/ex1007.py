class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        num_1 = 0
        num_2 = 1
        num_3 = 1
        num_4 = 0
        for i in range(1, len(A)):
            if A[i] == A[0]:
                continue
            elif B[i] == A[0]:
                num_1 += 1
            else:
                num_1 = float("Inf")
                break
        for i in range(1, len(A)):
            if A[i] == B[0]:
                continue
            elif B[i] == B[0]:
                num_2 += 1
            else:
                num_2 = float("Inf")
                break
        for i in range(1, len(A)):
            if B[i] == A[0]:
                continue
            elif A[i] == A[0]:
                num_3 += 1
            else:
                num_3 = float("Inf")
                break
        for i in range(1, len(A)):
            if B[i] == B[0]:
                continue
            elif A[i] == B[0]:
                num_4 += 1
            else:
                num_4 = float("Inf")
                break
        ans = min(num_1, num_2, num_3, num_4)
        return ans if ans!=float("Inf") else -1