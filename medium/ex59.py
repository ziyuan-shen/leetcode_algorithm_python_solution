class Solution:
    def fillCircle(self, matrix, idx, num, k):
        if k == 1:
            matrix[idx][idx] = num
        else:
            for c in range(idx, idx+k-1):
                matrix[idx][c] = num
                num += 1
            for r in range(idx, idx+k-1):
                matrix[r][idx+k-1] = num
                num += 1
            for c in range(idx+k-1, idx, -1):
                matrix[idx+k-1][c] = num
                num += 1
            for r in range(idx+k-1, idx, -1):
                matrix[r][idx] = num
                num += 1
            
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        for idx, k in enumerate(range(n, 0, -2)):
            self.fillCircle(matrix, idx, num, k)
            num += 4 * k - 4
        return matrix
        