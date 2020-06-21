class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                triangle[row][i] += min(triangle[row+1][i], triangle[row+1][i+1])
        return triangle[0][0]