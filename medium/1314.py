class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        length = len(mat)
        width = len(mat[0])
        ps = [[0 for _ in range(width + 1)] for _ in range(length + 1)]
        for i in range(1, width + 1):
            ps[1][i] = mat[0][i-1] + ps[1][i-1]
        for i in range(2, length + 1):
            for j in range(1, width + 1):
                ps[i][j] = mat[i-1][j-1] + ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1]
        ans = [[0 for _ in range(width)] for _ in range(length)]
        for i in range(length):
            for j in range(width):
                ans[i][j] = ps[min(i+K, length-1) + 1][min(j+K, width-1) + 1] - (ps[max(0, i-K)][min(j+K, width-1) + 1] + ps[min(i+K, length-1) + 1][max(0, j-K)] - ps[max(0, i-K)][max(0, j-K)])
        return ans