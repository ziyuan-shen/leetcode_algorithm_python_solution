class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        self.ans = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[i])-1, -1, -1):
                row.append(abs(A[i][j] - 1))
            self.ans.append(row)
        return self.ans
