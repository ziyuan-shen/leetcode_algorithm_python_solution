class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        width = len(matrix)
        length = len(matrix[0])
        low = 0
        high = width * length - 1
        mid = (low + high) // 2
        while low <= high:
            x, y = mid // length, mid % length
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                low = mid + 1
                mid = (low + high) // 2
            else:
                high = mid - 1
                mid = (low + high) // 2
        return False