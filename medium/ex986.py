class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        while A and B:
            if B[0][1] < A[0][0]:
                B.pop(0)
            elif A[0][1] < B[0][0]:
                A.pop(0)
            else:
                if B[0][1] <= A[0][1]:
                    ans.append([max(A[0][0], B[0][0]), B[0][1]])
                    B.pop(0)
                else:
                    ans.append([max(A[0][0], B[0][0]), A[0][1]])
                    A.pop(0)
        return ans