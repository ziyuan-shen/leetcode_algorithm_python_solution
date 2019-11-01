class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagicSquare(grid):
            flatten = [i for row in grid for i in row]
            flatten.sort()
            if not flatten == list(range(1, 10)):
                return False
            target = sum(grid[0])
            for i in range(3):
                if sum(grid[i]) != target:
                    return False
                if (grid[0][i]+grid[1][i]+grid[2][i]) != target:
                    return False
            diag_sum = 0
            reverse_diag_sum = 0
            for i in range(3):
                diag_sum += grid[i][i]
                reverse_diag_sum += grid[2-i][i]
            if diag_sum != target or reverse_diag_sum != target:
                return False
            return True
        
        if len(grid)<3 or len(grid[0])<3:
            return 0
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                subgrid = [grid[row][j:j+3] for row in range(i, i+3)]
                if isMagicSquare(subgrid):
                    count += 1
        return count