class Solution:
    def binarySearch(self, l, target):
        low = 0
        high = len(l) - 1
        while low <= high:
            mid = (low+high) // 2
            if l[mid] == target:
                return True
            elif l[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
    
    def getMatrix(self, row1, col1, row2, col2, matrix):
        if row2 < row1 or col2 < col1:
            return []
        return [row[col1:(col2+1)] for row in matrix[row1:(row2+1)]]
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        nrow = len(matrix)
        ncol = len(matrix[0])
        if nrow == 1:
            return self.binarySearch(matrix[0], target)
        elif ncol == 1:
            return self.binarySearch([row[0] for row in matrix], target)
        else:
            midrow = nrow // 2
            midcol = ncol // 2
            if matrix[midrow][midcol] == target:
                return True
            elif target > matrix[midrow][midcol]:
                if self.searchMatrix(self.getMatrix(midrow+1, midcol+1, nrow-1, ncol-1, matrix), target):
                    return True
                elif self.searchMatrix(self.getMatrix(0, midcol+1, midrow, ncol-1, matrix), target):
                    return True
                else:
                    return self.searchMatrix(self.getMatrix(midrow+1, 0, nrow-1, midcol, matrix), target)
            else:
                if self.searchMatrix(self.getMatrix(0, 0, midrow-1, midcol-1, matrix), target):
                    return True
                elif self.searchMatrix(self.getMatrix(0, midcol, midrow-1, ncol-1, matrix), target):
                    return True
                else:
                    return self.searchMatrix(self.getMatrix(midrow, 0, nrow-1, midcol-1, matrix), target)
                