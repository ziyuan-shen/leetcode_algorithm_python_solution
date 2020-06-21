"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 0:
            return None
        n = len(grid)
        val = grid[0][0]
        for i in range(n):
            for j in range(n):
                if grid[i][j] != val:
                    return Node(val, 0, self.construct([[grid[row][col] for col in range(n//2)] for row in range(n//2)]), self.construct([[grid[row][col] for col in range(n//2, n)] for row in range(n//2)]), self.construct([[grid[row][col] for col in range(n//2)] for row in range(n//2, n)]), self.construct([[grid[row][col] for col in range(n//2, n)] for row in range(n//2, n)]))
        return Node(val, 1, None, None, None, None)