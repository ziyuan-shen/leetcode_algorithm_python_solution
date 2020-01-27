class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        r = 0
        c = 0
        ans = [matrix[0][0]]
        while not (r == nrow - 1 and c == ncol - 1):
            while r - 1 >= 0 and c + 1 < ncol:
                r = r - 1
                c = c + 1
                ans.append(matrix[r][c])
            if c + 1 < ncol:
                c = c + 1
                ans.append(matrix[r][c])
            elif r + 1 < nrow:
                r = r + 1
                ans.append(matrix[r][c])
            while r + 1 < nrow and c - 1 >= 0:
                r = r + 1
                c = c - 1
                ans.append(matrix[r][c])
            if r + 1 < nrow:
                r += 1
                ans.append(matrix[r][c])
            elif c + 1 < ncol:
                c += 1
                ans.append(matrix[r][c])
        return ans