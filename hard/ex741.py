class Solution:
    def get_cherry(self, grid):
        '''
        returns:
        int: number of cherries collected
        list[list]: updated grid after collection
        bool: if there is a valid path
        '''
        nrow = len(grid)
        ncol = len(grid[0])
        current_node = grid[0][0]
        if current_node == -1:
            return 0, grid, False
        current_cherry = current_node
        if nrow > 1 and ncol > 1:
            right_cherry, right_grid, right_valid = self.get_cherry([row[1:] for row in grid])
            down_cherry, down_grid, down_valid = self.get_cherry(grid[1:])
            if right_cherry > down_cherry:
                new_grid = [[grid[i][0]] + right_grid[i] for i in range(nrow)]
                new_grid[0][0] = 0
                return current_cherry + right_cherry, new_grid, True
            else:
                if down_valid:
                    new_grid = [grid[0]] + down_grid
                    new_grid[0][0] = 0
                    return current_cherry + down_cherry, new_grid, True
                else:
                    return 0, grid, False
        else:
            if nrow == 1 and ncol == 1:
                return current_cherry, [[0]], True
            if nrow == 1:
                right_cherry, right_grid, right_valid = self.get_cherry([grid[0][1:]])
                if right_valid:
                    return current_cherry + right_cherry, [[0] + right_grid[0]], True
                else:
                    return 0, grid, False
            if ncol == 1:
                down_cherry, down_grid, down_valid = self.get_cherry(grid[1:])
                if down_valid:
                    return current_cherry + down_cherry, [[0]] + down_grid, True
                else:
                    return 0, grid, False
                
    def cherryPickup(self, grid: List[List[int]]) -> int:
        cherry, new_grid, valid = self.get_cherry(grid)
        if valid:
            cherry += self.get_cherry([row[::-1] for row in new_grid[::-1]])[0]
            return cherry
        else:
            return 0