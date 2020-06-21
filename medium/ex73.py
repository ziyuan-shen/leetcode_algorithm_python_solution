class Solution:
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        width = len(matrix[0])
        for i in range(length):
            for j in range(width):
                if matrix[i][j] == 0:
                    for row in range(length):
                        if matrix[row][j] != 0:
                            matrix[row][j] = float("inf")
                    for col in range(width):
                        if matrix[i][col] != 0:
                            matrix[i][col] = float("inf")
        for i in range(length):
            for j in range(width):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0