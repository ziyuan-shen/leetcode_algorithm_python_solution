class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        nrow = len(matrix)
        ncol = len(matrix[0])
        maxwidth = [[0 for _ in range(ncol)] for _ in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == '1':
                    maxwidth[i][j] = maxwidth[i][j-1] + 1 if j >= 1 else 1
        ans = 0
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == '1':
                    maxarea = 0
                    width = maxwidth[i][j]
                    for k in range(i, -1, -1):
                        width = min(width, maxwidth[k][j])
                        maxarea = max(maxarea, width * (i-k+1))
                    if maxarea > ans:
                        ans = maxarea
        return ans