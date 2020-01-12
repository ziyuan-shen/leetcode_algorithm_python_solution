class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for t in range(n - 1 - 2 * i):
                temp = [matrix[i][-i-1-t], matrix[i+t][i], matrix[-i-1][i+t], matrix[-i-1-t][-i-1]]
                matrix[i][-i-1-t] = temp[1]
                matrix[i+t][i] = temp[2]
                matrix[-i-1][i+t] = temp[3]
                matrix[-i-1-t][-i-1] = temp[0]