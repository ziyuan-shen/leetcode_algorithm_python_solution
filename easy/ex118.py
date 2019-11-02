class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        triangle = self.generate(numRows-1)
        row = [1]
        for i in range(numRows-2):
            row.append(triangle[-1][i]+triangle[-1][i+1])
        row.append(1)
        triangle.append(row)
        return triangle