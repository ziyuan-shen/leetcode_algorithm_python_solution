class Solution:
    def setRowCol(self, matrix, row, col):
        self.zero_nodes.add((row, col))
        for i in range(len(matrix[0])):
            if matrix[row][i] == 0 and (row, i) not in self.zero_nodes:
                self.setRowCol(matrix, row, i)
            matrix[row][i] = 0
            self.zero_nodes.add((row, i))
        for i in range(len(matrix)):
            if matrix[i][col] == 0 and (i, col) not in self.zero_nodes:
                self.setRowCol(matrix, i, col)
            matrix[i][col] = 0
            self.zero_nodes.add((i, col))
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.zero_nodes = set()
        length = len(matrix)
        width = len(matrix[0])
        for i in range(length):
            for j in range(width):
                if (i, j) not in self.zero_nodes:
                    if matrix[i][j] == 0:
                        self.setRowCol(matrix, i, j)
                        break