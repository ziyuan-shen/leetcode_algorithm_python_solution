class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        perimeter = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    for neighbor in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if neighbor[0] >= 0 and neighbor[0] < length and neighbor[1] >= 0 and neighbor[1] < width:
                            if grid[neighbor[0]][neighbor[1]] == 0:
                                perimeter += 1
                        else:
                            perimeter += 1
        return perimeter