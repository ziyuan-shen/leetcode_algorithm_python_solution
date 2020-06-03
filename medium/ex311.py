class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        lengtha = len(A)
        widthb = len(B[0])
        widtha = len(A[0])
        ans = [[0 for _ in range(widthb)] for _ in range(lengtha)]
        for i in range(lengtha):
            for j in range(widthb):
                num = 0
                for k in range(widtha):
                    num += A[i][k] * B[k][j]
                ans[i][j] = num
        return ans