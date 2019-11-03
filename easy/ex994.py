class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minute = 0
        while True:
            change_flag = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        adjacent_nodes = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
                        for node in adjacent_nodes:
                            if node[0]>=0 and node[0]<len(grid) and node[1]>=0 and node[1]<len(grid[0]):
                                if grid[node[0]][node[1]] == 1:
                                    grid[node[0]][node[1]] = 3
                                    change_flag = True
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
            if change_flag:
                minute += 1
            else:
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j] == 1:
                            return -1
                return minute