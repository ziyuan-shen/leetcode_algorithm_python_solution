from bisect import bisect_left

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        width = len(matrix[0])
        ps = [[0 for _ in range(width+1)] for _ in range(length+1)]
        for i in range(1, length + 1):
            for j in range(1, width + 1):
                ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + matrix[i-1][j-1]
        ans = float("-inf")
        for row1 in range(1, length + 1):
            for row2 in range(row1, length + 1):
                array = [0]
                for col in range(1, width + 1):
                    cum_area = ps[row2][col] - ps[row1-1][col]
                    idx = bisect_left(array, cum_area - k)
                    if idx < len(array):
                        ans = max(ans, cum_area - array[idx])
                    idx = bisect_left(array, cum_area)
                    array.insert(idx, cum_area)
        return ans