class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        if nrow < 3 or ncol < 3:
            if nrow == 1:
                return matrix[0]
            if ncol == 1:
                return [row[0] for row in matrix]
            if nrow == 2:
                return matrix[0] + matrix[1][::-1]
            if ncol == 2:
                return [matrix[0][0]] + [row[1] for row in matrix] + [row[0] for row in matrix[-1:0:-1]]
        else:
            return matrix[0] + [row[-1] for row in matrix[1:-1]] + matrix[-1][::-1] + [row[0] for row in matrix[-2:0:-1]] + self.spiralOrder([row[1:-1] for row in matrix[1:-1]])